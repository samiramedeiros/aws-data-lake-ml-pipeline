import sys
from awsglue.context import GlueContext # type: ignore
from awsglue.job import Job # type: ignore
from pyspark.context import SparkContext # type: ignore
from awsglue.utils import getResolvedOptions # type: ignore
from pyspark.sql.functions import count, sum, avg # type: ignore

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

# Ler PROCESSED
df = spark.read.parquet(
    "s3://banking-data-lake-sm/processed/transactions/"
)

# Métricas de risco (exemplo)
risk_df = (
    df.groupBy("customer_id")
      .agg(
          count("*").alias("total_transactions"),
          sum("amount").alias("total_amount"),
          avg("amount").alias("avg_amount")
      )
)

# Gravar CURATED
risk_df.write.mode("overwrite").parquet(
    "s3://banking-data-lake-sm/curated/risk_analysis/"
)

job.commit()
