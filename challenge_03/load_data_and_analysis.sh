source ../challenge_01_02/.env

# set PGPASSWORD to avoid password prompt

export PGPASSWORD=${POSTGRES_PASSWORD}

# Create the tables in the database
psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -d ${POSTGRES_DB} -U ${POSTGRES_USER} -f table_script_creation.sql;

# truncate the tables to ensure they are empty before loading new data
psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -d ${POSTGRES_DB} -U ${POSTGRES_USER} -f truncate_tables.sql; 

# Load the data into the tables

path_input_data_products="${DATA_PATH_FILES_INPUT}products.csv"
path_input_data_orders="${DATA_PATH_FILES_INPUT}orders.csv"
 
load_orders="\copy products (id,name,category,price) FROM  ${path_input_data_products} WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE);"
load_products="\copy orders (id,product_id,quantity,created_date) FROM  ${path_input_data_orders} WITH (FORMAT CSV, DELIMITER ',', HEADER TRUE);"

psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -d ${POSTGRES_DB} -U ${POSTGRES_USER}  -c "${load_orders}"
psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -d ${POSTGRES_DB} -U ${POSTGRES_USER}  -c "${load_products}"

# Run the analysis script

psql -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} -d ${POSTGRES_DB} -U ${POSTGRES_USER} -f kpi_analysis.sql

unset PGPASSWORD