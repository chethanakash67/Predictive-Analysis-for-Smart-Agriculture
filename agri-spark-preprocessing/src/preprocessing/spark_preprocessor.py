class SparkPreprocessor:
    def __init__(self, spark):
        self.spark = spark

    def load_data(self, path: str):
        """Loads data from the specified path into a Spark DataFrame."""
        df = self.spark.read.csv(path, header=True, inferSchema=True)
        return df

    def clean_data(self, df):
        """Cleans the DataFrame by handling missing values and duplicates."""
        df = df.dropDuplicates()
        df = df.na.drop()
        return df

    def transform_data(self, df):
        """Applies transformations to the DataFrame, such as encoding categorical variables."""
        # Example transformation: One-hot encoding for categorical variables
        categorical_cols = [col for col, dtype in df.dtypes.items() if dtype == 'string']
        for col in categorical_cols:
            df = df.withColumn(col, df[col].cast("string"))
            df = df.withColumn(col, df[col].cast("string"))
        return df

    def save_data(self, df, path: str):
        """Saves the processed DataFrame to the specified path."""
        df.write.csv(path, header=True)