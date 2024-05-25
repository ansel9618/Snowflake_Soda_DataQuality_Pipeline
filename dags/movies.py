from airflow.decorators import dag, task
from datetime import datetime
from airflow.models.baseoperator import chain

from astro import sql as aql
from astro.files import File
from astro.sql.table import Table

@aql.transform
def top_10_movies(input_table: Table):
    return """
           SELECT "Title","Rating"
           FROM {{ input_table }}
           ORDER BY "Rating" DESC
           LIMIT 10 
           """

@dag(
    start_date=datetime(2024, 5, 21),
    schedule='@daily',
    catchup=False,
    tags=['movie']
)
def movie():
    
    load_movie_to_snowflake = aql.load_file(
        task_id='load_movie_to_snowflake',
        input_file=File(
            path='https://raw.githubusercontent.com/ansel9618/Dataquality_Pipeline_AirflowSnowflake_Soda/main/data/imdb.csv'  # Use raw link for direct access
        ),
        output_table=Table(
            name='movie',
            conn_id='snowflake'
        )
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_movie(scan_name='check_movie',checks_subpath='tables',data_source='snowflake_db'):
        from include.soda.check_function import check

        return check(scan_name, checks_subpath, data_source)

    top_table = top_10_movies(
        input_table=Table(name='movie', conn_id='snowflake'),
        output_table=Table(name='top_movie', conn_id='snowflake')
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_top_movie(scan_name='check_top_movie',checks_subpath='tables',data_source='snowflake_db'):
        from include.soda.check_function import check

        return check(scan_name, checks_subpath, data_source)

    chain(load_movie_to_snowflake , check_movie(), top_table, check_top_movie())
movie()
