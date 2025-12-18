import sys
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from pyspark.context import SparkContext  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.sql.functions import (
    count,
    sum as _sum,
    avg
)

# Inicialização
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# Leitura PROCESSED
processed_df = spark.read.parquet(
    "s3://banking-data-lake-sm/processed/transactions/"
)

# Feature Engineering (ML Features)
ml_features_df = (
    processed_df
    .groupBy("customer_id")
    .agg(
        count("*").alias("transaction_count"),
        _sum("amount").alias("total_amount"),
        avg("amount").alias("avg_transaction_amount")
    )
)

# Escrita CURATED / ML FEATURES
ml_features_df.write.mode("overwrite").parquet(
    "s3://banking-data-lake-sm/curated/ml_features/"
)

job.commit()
