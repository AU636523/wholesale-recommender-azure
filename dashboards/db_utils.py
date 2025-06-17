import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Paths
ROOT_PATH = "c:/sparkdata/wholesale-recommender"
CLEANED_DATA_PATH = os.path.join(ROOT_PATH, "results")
PROCESSED_DATA_PATH = os.path.join(ROOT_PATH, "processed")
RESULTS_DATA_PATH = os.path.join(ROOT_PATH, "results")

# Init Spark session
spark = SparkSession.builder \
    .appName("Spark Session for Dashboard") \
    .getOrCreate()

def load_customer_ids(parquet_path):
    # Load data
    df = spark.read.parquet(parquet_path)

    # Extract unique customer IDs
    customer_ids_df = df.select("Customer ID").distinct()

    return customer_ids_df

# %%
if __name__ == "__main__":
    
    CUSTOMER_FEATURES_PATH = os.path.join(PROCESSED_DATA_PATH, "customers_features") 
    
    # Load and show
    customer_ids = load_customer_ids(CUSTOMER_FEATURES_PATH)
    customer_ids.show()
