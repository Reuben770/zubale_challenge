**Question 2**: What ETL/ELT tool would you use to extract this data and insert it into BigQuery? 

To answer this question, I'd like to present different scenarios:

1- Postgres Database is allocated in on premise:
   - **Extract the Data (E)**. Run and psql script in the on-premise solution and extract the data for all the tables you need to load to bigquery, for example orders by an incremental date and products.
   - **Upload to GCS (Google Cloud Storage)**. The next step is to upload the data to GCS, tipicaly a landing area
   - **Load to Bigquery (LT)**. The next and the finaly, is load the data to a bigquery table, previusly created. To upload the data, it's recommendable to use some orchestration platform like airflow, or in the case of GCP, composer.
   - **Orchestration**. As I mentioned before, this step enables you to load the data finally to Bigquery using a DAG doing some tasks internally  

        start-load-->read_config-->move_landing2clean-->load_staging-->check_some_rules-->sync_final_table-->post-load-sync-->move_to_processed-->end_load
 
        Each step internaly in the DAG is responsably for specific tasks

        - **read_config**. Read some parameters in order to get more information about the process, for example table schema, delimiter, extension, file type (CSV, JSONL, etc) rules to by apply finaly
        - **move_landing2clean**. Move the raw file from the landing --> clean area
        - **load_staging** . Load the data to a temporay table, in bigquery, to further apply some rules to validate the data. Internally this step is using the Bigquery API to load from GCS file to a table.
        - **check_some_rules**: Execute some rules, dynamically to check if there are some alerts to check and not to continue in the process.
        - **sync_final_table**:  Load finally the data from tmp table (staging) to the final table.
        - **post-load-sync**. If there are some post load actions to be done, you can do in this step.
        - **move_to_processed**. Move the file form clea are to raw area for historical reasons.

2- Postgres Database is allocated in GCP (Cloud Sql):
   - **Extract the Data (EL)**. This stage is not required because you can create an external conection in BigQuery to extract directery from external table and integrate in Bigquery.
   - **Orquestation**. In this approach requires other DAG in composer because it doesn’t respond to the same architecture defined in the previus scenario. But the idea of these DAGs will be to simplify some tasks and change others, for example the stage for **load_staging** must be replaced by the native integration by external table in Bigquery.
3- Postgres Database is allocated in GCP (Cloud Sql or Standalone):    
   - **Extract the Data (E)**. Run and psql script or a job in the Cloud to extract the data from the database and load directly to GCS.
   - **Load to Bigquery (LT)** and **Orchestration** will be the same as the first scenario.

**Question 3**: What AI-based pipeline could you add to this pipeline? 
   - **Scope**: Based on the definition for AI-based I'm considering specific machine learning models to generate prediction about specific scenarios, ie: predict future demand.
    - **Main steps to integrate**:
        a. **Data Source**: It's required to identify the sources for the scope.
        b. **Data Preparation for ML (within BigQuery)**: It's probably required to create some aggregation to simplify the data, preprocess the data input to prepare for the model, next step. 
        c. **Model Training (AI Component)**: To train the model it's required historical data, and the approach will be to use the native Bigquery ML we based on the scope.
        d. **Model Evaluation (AI Component)**: After training, it's required to evaluate the model based in accuracy and other metrics.
        e. **Prediction (AI Component)**: The trained and evaluated model is then used to generate predictions, and the result will be stored in Bigquery.
        f. **Storing Predictions**: The result of the previous step will be stored in a new bigquery table.
        h. **Serving/Visualization**: The data generated you can access by visualization tools like Looker Studio or will be available to integrate in other operational systems.
        i. **Orchestration**: To orchestrate the end-to-end process you can use composer/airflow.
