from pyspark.sql import DataFrame
from typing import Dict, Any

class DataFrameSchema:
    def __init__(self, schema: Dict[str, Any]):
        self.schema = schema

class PreprocessingConfig:
    def __init__(self, config: Dict[str, Any]):
        self.config = config