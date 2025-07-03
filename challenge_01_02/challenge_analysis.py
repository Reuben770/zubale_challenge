from dotenv import load_dotenv 
import pandas as pd
import os
import freecurrencyapi

load_dotenv()

DATA_PATH_FILES_INPUT = os.getenv("DATA_PATH_FILES_INPUT")
DATA_PATH_FILES_OUTPUT = os.getenv("DATA_PATH_FILES_OUTPUT")
API_KEY_FREECURRENCY = os.getenv("API_KEY_FREECURRENCY")


def challenge_01() -> pd.DataFrame:
    """ 
    Challenge 01: Merge Orders and Products DataFrames and Calculate Total Price

    This function loads the products and orders data from CSV files, merges them,
    calculates the total price for each order, and saves the result to a new CSV file.
    
    """
    # Check if the environment variable is set and the path exists
    # Load the products and orders data from CSV files

    df_products = pd.read_csv(DATA_PATH_FILES_INPUT + "products.csv") 
    df_orders   = pd.read_csv(DATA_PATH_FILES_INPUT + "orders.csv")


    # Merge the orders and products DataFrames on product_id
    df_merge = pd.merge(df_orders, df_products, left_on='product_id', right_on="id", how='inner')

    # Rename columns for clarity
    df_order_full = df_merge.rename(columns={
        "created_date": "order_created_date",
        "id_x": "order_id",
        "name" :"product_name"} )

    # Calculate the total price for each order
    df_order_full["total_price"]= df_order_full["quantity"] * df_order_full["price"]

    # Save the final DataFrame to a CSV file

    df_order_full[["order_id", "order_created_date", "product_name", "quantity",  "total_price"]].to_csv(DATA_PATH_FILES_OUTPUT + "order_full_information.csv", index=False)

    return df_order_full


def challenge_02(df_order_full: pd.DataFrame) -> None:
    """ Challenge 02: Convert Total Price from BRL to USD
    
    This function converts the total price of orders from BRL to USD using the FreeCurrency API.
    It fetches the latest exchange rates and saves the updated DataFrame to a new CSV file.
    It assumes that the total price in the DataFrame is in BRL and converts it to USD.
    It also renames the total price column to indicate the currency.
    It requires the API_KEY_FREECURRENCY environment variable to be set for accessing the FreeCurrency API.
    It uses the freecurrencyapi library to fetch the exchange rates.
    The resulting DataFrame is saved to a CSV file named "fixed_order_full_information.csv"

    """

    # Initialize the FreeCurrency API client
    client = freecurrencyapi.Client(API_KEY_FREECURRENCY)

    # Fetch latest exchange rates
    result = client.latest(base_currency='USD', currencies=['BRL'])

    # Convert total_price from BRL to USD using the exchange rate

    df_order_full["total_price_usd"]= df_order_full["total_price"] * result["data"]["BRL"] 

    # Rename columns for clarity
    df_order_full_new = df_order_full.rename(columns={
        "total_price": "total_price_br" } )

    df_order_full_new[["order_id", "order_created_date", "product_name", "quantity",  "total_price_br","total_price_usd"]].to_csv(DATA_PATH_FILES_OUTPUT + "fixed_order_full_information.csv", index=False)


def   challenge_02_1(df_order_full: pd.DataFrame) -> None:
    """ Challenge 02.1: Calculate KPIs from Orders DataFrame
    
    This function calculates key performance indicators (KPIs) from the orders DataFrame.
    It groups the data by order creation date, product name, and category to find the top
    order date, product, and category based on total quantity and total price.
    It saves the results to a CSV file named "kpi_product_orders.csv".

    """

    df1=df_order_full.groupby("order_created_date").agg(
        total_quantity=('quantity', 'sum'),
        total_price_usd=('total_price_usd', 'sum'),
        order_count=('order_id', 'count')
    ).reset_index().sort_values(by="order_count", ascending=False).head(1)

    df2=df_order_full.groupby("product_name").agg(
        total_quantity=('quantity', 'sum'),
        total_price_usd=('total_price_usd', 'sum'),
        order_count=('order_id', 'count')
        ).reset_index().sort_values(by="total_quantity", ascending=False).head(1)

    df3=df_order_full.groupby("category").agg(
        total_quantity=('quantity', 'sum'),
        total_price_usd=('total_price_usd', 'sum'),
        order_count=('order_id', 'count')
        ).reset_index().sort_values(by="total_quantity", ascending=False).head(3) 


    # Create a list of DataFrames for each KPI
    df_resultado=[df1,df2,df3]

    # Define labels for each KPI DataFrame
    labels = ['KP1', 'KP2', 'KP3']

    # Combine the DataFrames into a single DataFrame with hierarchical indexing
    df_combined = pd.concat(df_resultado, keys=labels).reset_index()

    # Clear NAN for a default value
    df_combined.fillna("", inplace=True)

    # Rename the 'level_0' column to 'kpi_name'
    df_combined.rename(columns={
        "level_0": "kpi_name" }, inplace=True )

    df_combined[["kpi_name", "order_created_date", "product_name", "category",  "total_quantity","total_price_usd","order_count"]].to_csv(DATA_PATH_FILES_OUTPUT + "kpi_product_orders.csv", index=False)


if __name__ == "__main__":
    # Execute the challenges

    print("Executing Challenge 01, 02 and 02.1")
   
    if not DATA_PATH_FILES_INPUT or not DATA_PATH_FILES_OUTPUT or not API_KEY_FREECURRENCY: 
        raise ValueError("DATA_PATH_FILES,DATA_PATH_FILES_OUTPUT or API_KEY_FREECURRENCY environment variable is not set.")    
    else:
        if not os.path.exists(DATA_PATH_FILES_INPUT):
            raise FileNotFoundError(f"The specified path {DATA_PATH_FILES_INPUT} does not exist.")
        
        if not os.path.exists(DATA_PATH_FILES_OUTPUT):
            raise FileNotFoundError(f"The specified path {DATA_PATH_FILES_OUTPUT} does not exist.")        
        
        if not os.path.exists(DATA_PATH_FILES_INPUT + "products.csv"):
            raise FileNotFoundError(f"The products.csv file does not exist in the specified path {DATA_PATH_FILES_INPUT}.")

        if not os.path.exists(DATA_PATH_FILES_INPUT + "orders.csv"):
            raise FileNotFoundError(f"The orders.csv file does not exist in the specified path {DATA_PATH_FILES_INPUT}.")

    df_order_full = challenge_01()
    print("Challenge 01 completed.")

    challenge_02(df_order_full)

    print("Challenge 02 completed.")

    challenge_02_1(df_order_full)    

    print("Challenge 02_1 completed.")

    print("Challenges completed. Results saved to CSV files.")
    print(f"Check the files in the path: {DATA_PATH_FILES_OUTPUT}")
    