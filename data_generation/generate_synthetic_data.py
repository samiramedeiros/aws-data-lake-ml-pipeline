"""
Gera dados sintéticos de transações bancárias.
Esses dados simulam a camada RAW do Data Lake.
"""

import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Quantidade de registros
NUM_RECORDS = 1000

# Tipos de transação
TRANSACTION_TYPES = ["PIX", "CREDIT", "DEBIT", "TED"]

def generate_transactions(num_records: int) -> pd.DataFrame:
    data = []

    start_date = datetime.now() - timedelta(days=1)

    for i in range(num_records):
        record = {
            "transaction_id": i + 1,
            "customer_id": random.randint(1000, 1100),
            "amount": round(random.uniform(10, 5000), 2),
            "transaction_type": random.choice(TRANSACTION_TYPES),
            "timestamp": start_date + timedelta(minutes=random.randint(0, 1440))
        }
        data.append(record)

    return pd.DataFrame(data)

def main():
    df = generate_transactions(NUM_RECORDS)

    os.makedirs("data", exist_ok=True)
    output_path = "data/transactions.csv"

    df.to_csv(output_path, index=False)
    print(f"Arquivo gerado com sucesso em: {output_path}")

if __name__ == "__main__":
    main()
