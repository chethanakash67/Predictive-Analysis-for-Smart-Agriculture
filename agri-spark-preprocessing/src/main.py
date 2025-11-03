import pyspark
from pyspark.sql import SparkSession
from preprocessing.spark_preprocessor import SparkPreprocessor

def main():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Agricultural Data Preprocessing") \
        .getOrCreate()

    # Create an instance of the SparkPreprocessor
    preprocessor = SparkPreprocessor(spark)

    # Define the path to the input data and output data
    input_data_path = "path/to/input/data.csv"
    output_data_path = "path/to/output/processed_data.csv"

    # Load data
    df = preprocessor.load_data(input_data_path)

    # Clean data
    cleaned_df = preprocessor.clean_data(df)

    # Transform data
    transformed_df = preprocessor.transform_data(cleaned_df)

    # Save processed data
    preprocessor.save_data(transformed_df, output_data_path)

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    main()