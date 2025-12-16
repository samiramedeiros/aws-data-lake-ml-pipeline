"""
Geração de dados sintéticos de transações bancárias.
Camada RAW do Data Lake.
Formato: Parquet
Particionado por year/month/day
"""

import pandas as pd
import random
from datetime import datetime
import os

# ======================
# Configurações
# ======================
NUM_RECORDS = 1000
BASE_OUTPUT_PATH = "data/raw/transactions"

TRANSACTION_TYPES = ["PIX", "CREDIT", "DEBIT", "TED"]

# ======================
# Geração dos dados
# ======================
def generate_transactions(num_records: int) -> pd.DataFrame:
    records = []
    now = datetime.now()

    for i in range(num_records):
        records.append({
            "transaction_id": i + 1,
            "customer_id": random.randint(1000, 1100),
            "amount": round(random.uniform(10, 5000), 2),
            "transaction_type": random.choice(TRANSACTION_TYPES),
            "timestamp": now
        })

    return pd.DataFrame(records)

# ======================
# Escrita particionada
# ======================
def write_parquet_partitioned(df: pd.DataFrame) -> None:
    df["year"] = df["timestamp"].dt.year
    df["month"] = df["timestamp"].dt.month.astype(str).str.zfill(2)
    df["day"] = df["timestamp"].dt.day.astype(str).str.zfill(2)

    year = df["year"].iloc[0]
    month = df["month"].iloc[0]
    day = df["day"].iloc[0]

    output_path = f"{BASE_OUTPUT_PATH}/year={year}/month={month}/day={day}"
    os.makedirs(output_path, exist_ok=True)

    file_path = f"{output_path}/transactions.parquet"

    df.drop(columns=["year", "month", "day"]).to_parquet(
        file_path,
        index=False,
        engine="pyarrow"
    )

    print(f"Arquivo Parquet gerado em: {file_path}")

# ======================
# Main
# ======================
def main():
    df = generate_transactions(NUM_RECORDS)
    write_parquet_partitioned(df)

if __name__ == "__main__":
    main()
