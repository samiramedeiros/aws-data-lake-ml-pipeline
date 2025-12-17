import sys
from awsglue.context import GlueContext  # type: ignore
from awsglue.job import Job  # type: ignore
from pyspark.context import SparkContext  # type: ignore
from awsglue.utils import getResolvedOptions  # type: ignore
from pyspark.sql.functions import col, to_date, count, sum, avg  # type: ignore

# Inicialização
args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# Leitura PROCESSED
df = spark.read.parquet(
    "s3://banking-data-lake-sm/processed/transactions/"
)

# Transformações CURATED
curated_df = (
    df
    .withColumn("date", to_date(col("timestamp")))
    .groupBy("date")
    .agg(
        count("*").alias("total_transactions"),
        sum("amount").alias("total_amount"),
        avg("amount").alias("avg_transaction_amount")
    )
)

# Escrita CURATED
curated_df.write.mode("overwrite").parquet(
    "s3://banking-data-lake-sm/curated/daily_transaction_metrics/"
)

job.commit()
