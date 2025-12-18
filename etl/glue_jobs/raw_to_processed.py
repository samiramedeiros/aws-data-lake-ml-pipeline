import sys
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from pyspark.context import SparkContext  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.sql.functions import col  # type: ignore

# Inicialização
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# Leitura RAW
raw_df = spark.read.parquet(
    "s3://banking-data-lake-sm/raw/transactions/"
)

# 🔧 CORREÇÃO DO TIMESTAMP (ESSENCIAL)
raw_df = raw_df.withColumn(
    "timestamp",
    col("timestamp").cast("timestamp")
)

# Transformações básicas
processed_df = (
    raw_df
    .filter(raw_df.amount > 0)
    .dropDuplicates(["transaction_id"])
)

# Escrita PROCESSED
processed_df.write.mode("overwrite").partitionBy(
    "year", "month", "day"
).parquet(
    "s3://banking-data-lake-sm/processed/transactions/"
)

job.commit()
