export PGPASSWORD=demo

# Create the tables in the database
psql -d base_demo -U demo -f table_script_creation.sql;

# Load the data into the tables
psql -d base_demo -U demo -f load_data.sql;

# Run the analysis script

psql -d base_demo -U demo -f kpi_analysis.sql;