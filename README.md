# Snowflake_Soda_DataQuality_Pipeline

## Data pipeline which loads data from a http endpoint to snowflake and with dataquality checks using Soda with the help of Airflow astro sdk

![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/1.0_.png)

### First step is to create a snowflake account
### The following database,schema need to be created in snowflake via a sql worksheet

```
CREATE DATABASE AIRFLOW_TUTORIAL_DB;

CREATE SCHEMA AIRFLOW_TUTORIAL_SCHEMA;
```
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/10.0_.png)

### Install the asto cli by referring the doc link :->([GitHub Pages](https://docs.astronomer.io/astro/cli/get-started-cli))

### once astro env is set up create connection to snowflake and aws via airflow and test them
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/5.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/6.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/7.0_.png)

### refer code in dag folder --> movies.py
##Data quality checks

Soda is one of the easiest dataquality tool that we can use to check the quality of our data
airflow has some data quality check operators but ultimately its an orchestrator
so its better to use SODA.

mention the follo: configuration inside .env file
```
SNOWFLAKE_USER='********'
SNOWFLAKE_PASSWORD='************'
SNOWFLAKE_ACCOUNT='******.ap-*****-1.aws'
```

now inside the include folder create another folder called soda and 
inside that folder create a configuration.yml file
refer ([configuration.yml](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/include/soda/configuration.yml))

Soda will be installed in a separate venv
we will create a separate python env to install soda in order to prevent dependency conflicts with airflow

refer docker file to see the packages installed and libraries to download ([configuration.yml](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/Dockerfile))


once this is done restart the docker container which has the airflow instance using command
```
astro dev restart
```
once airflow restarts we need to check whether the data source added in configuration.yml file inside the soda folder works
so once restarted we need to go tto the airflow bash terminal
```
>>> astro dev bash

inside the bash activate the soda_venv command

>>> source soda_venv/bin/activate

now we can check the snowflake connection suing command

>>> soda test-connection -d snowflake_db -c include/soda/
```
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/11.0_.png)


so we'll be writing one function to call both data quality checks
refer ([check_function.py](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/include/soda/check_function.py))

After above step we can now implement the actual checks
([movie.yml](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/include/soda/check_function.py))
([top_movie.yml](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/include/soda/check_function.py))

after this refer dag to see the implementation of checks using python external operator
and finally all the oprations are chained to form a dag

### Dag Execution and output

![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/4.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/8.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/9.0_.png)

### Tables created inside Snowflakedb

![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/2.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/3.0_.png)







