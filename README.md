# Snowflake_Soda_DataQuality_Pipeline

## Data pipeline which loads data from a http endpoint to snowflake and with dataquality checks using Soda with the help of Airflow astro sdk

![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/1.0_.png)

### First step is to create a snowflake account
### The following database,schema need to be created in snowflake via a sql worksheet

```
CREATE DATABASE AIRFLOW_TUTORIAL_DB;

CREATE SCHEMA AIRFLOW_TUTORIAL_SCHEMA;


```

### Install the asto cli by referring the doc link :->([GitHub Pages](https://docs.astronomer.io/astro/cli/get-started-cli))

### once astro env is set up create connection to snowflake and aws via airflow and test them
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/5.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/6.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/7.0_.png)

### refer code in dag folder --> movies.py



### Dag Execution and output

![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/4.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/8.0_.png)
![](https://github.com/ansel9618/Snowflake_Soda_DataQuality_Pipeline/blob/main/images/9.0_.png)






