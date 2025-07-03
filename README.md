## This repo you cand find all the script, input and output related to the techincal challenge.

1- Clone this repo in diretory previuse createad

```bash
    git clone -b orign  https://github.com/Reuben770/zubale_challenge.git .
```

2- Install all the requeriments.txt to execute some challenge

```bash
    pip install freecurrencyapi
    pip install -r requirements.txt 
```
3- Create .env and add all the variables required internally

    DATA_PATH_FILES_INPUT= # Path to the input directory where the raw data files are located
    DATA_PATH_FILES_OUTPUT= # Path to the output directory where the processed files will be saved
    API_KEY_FREECURRENCY= # API key for the FreeCurrency API to fetch exchange rates
    POSTGRES_DB= # Name of the PostgreSQL database to connect to
    POSTGRES_USER= # Username for the PostgreSQL database
    POSTGRES_PASSWORD= # Password for the PostgreSQL database user
    POSTGRES_HOST= # Hostname for the PostgreSQL database
    POSTGRES_PORT= # Port number for the PostgreSQL database connection

    The .env file must be in the challenge_01_02 directory

4- Execute python challenge_analysis.py to get the results of the challenge 1, 2, 3. This challenge_analysis.py internally has all the comments related to what's is doing, step by step.

```bash
    cd challenge_01_02
    python challenge_analysis.py
```

You will se this output 

Executing Challenge 01, 02 and 02.1
Challenge 01 completed.
Challenge 02 completed.
Challenge 02_1 completed.
Challenges completed. Results saved to CSV files.

In the ./data/output you will find 3 files:
    - order_full_information.csv
    - fixed_order_full_information.csv
    - kpi_product_orders.csv

Each file corresponds to the challenge required.   

5- To execute challenge 3 you need to follow these steps, but there are some pre requirement you need to have done:
  - valid Postgres database
  - configure in the .env this variables properly
        POSTGRES_DB= # Name of the PostgreSQL database to connect to
        POSTGRES_USER= # Username for the PostgreSQL database
        POSTGRES_PASSWORD= # Password for the PostgreSQL database user
        POSTGRES_HOST= # Hostname for the PostgreSQL database
        POSTGRES_PORT= # Port number for the PostgreSQL database connection
   - The bash command will create the tables, load the data an generate the results    

```bash
    cd challenge_03
    bash load_data_and_analysis.sh
```

After running this script, you will see this result:

```bash
psql:table_script_creation.sql:6: NOTICE:  relation "orders" already exists, skipping
CREATE TABLE
psql:table_script_creation.sql:9: NOTICE:  relation "idx_orders_product_id" already exists, skipping
CREATE INDEX
psql:table_script_creation.sql:16: NOTICE:  relation "products" already exists, skipping
CREATE TABLE
TRUNCATE TABLE
TRUNCATE TABLE
COPY 20
COPY 50
 order_created_date | total_quantity | total_price_usd | order_count 
--------------------+----------------+-----------------+-------------
 2024-12-06         |             29 |         1160.83 |          10
(1 row)

 product_name | total_quantity | total_price_usd | order_count 
--------------+----------------+-----------------+-------------
 Product_5    |             20 |          891.80 |           8
(1 row)

 category | total_quantity | total_price_usd | order_count 
----------+----------------+-----------------+-------------
 Shirts   |             50 |         3786.65 |          16
 Jackets  |             30 |          897.52 |          10
 Pants    |             29 |         1720.44 |          11
(3 rows)

```

If the table exist previously, you will see a warning about the creation table must be skipped.

6- Analysis the results of Challenge 4 

In the folder ./challenge_04 you will find these files:

   - **01_other_analysis.md** . Describe all the answers related to the first question.
   - **02_etl_integration_to_bigquery.md** . Describe all the answers related to the second and third question.

**Any question I will be available to solve and help you**
**Regards Ruben**
