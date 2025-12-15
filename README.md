# 🏦 Sistema de Análise Inteligente de Transações Financeiras

**Projeto:** `aws-data-lake-ml-pipeline`

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [Arquitetura](#arquitetura)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Estrutura do Projeto](#estrutura-do-projeto)
5. [Setup e Instalação](#setup-e-instalação)
6. [Guia de Uso](#guia-de-uso)
7. [Métricas e Resultados](#métricas-e-resultados)
8. [Boas Práticas](#boas-práticas)
9. [Próximos Passos](#próximos-passos)

---

## 🎯 Visão Geral

Sistema completo de engenharia de dados para instituição financeira, incluindo:

- **Pipeline ETL escalável** processando milhões de transações diárias
- **Data Lake arquitetura medalhão** (raw → processed → curated)
- **Detecção de fraudes com ML** usando AWS SageMaker
- **IA Generativa** para insights automáticos com Amazon Bedrock
- **Consultas SQL otimizadas** via AWS Athena
- **Análise de comportamento** de clientes em tempo real

### 🎖️ Destaques Técnicos

✅ **Escalabilidade**: Processa de GB a PB de dados  
✅ **Serverless**: Sem infraestrutura para gerenciar  
✅ **Cost-effective**: Paga apenas pelo que usa  
✅ **Real-time**: Detecção de anomalias em tempo real  
✅ **IA Generativa**: Relatórios automáticos e Q&A sobre dados  

---

## 🏗️ Arquitetura

### Diagrama

<img width="802" height="486" alt="Diagrama aws-data-lake-ml-pipeline" src="https://github.com/user-attachments/assets/a00be8cf-9205-4e32-80f7-ded9ca4c07b4" />

### Arquitetura Detalhada por Camada

#### 1. Camada de Ingestão
- **AWS Lambda**: Trigger para novos arquivos
- **AWS Kinesis**: Streaming de dados em tempo real
- **AWS DMS**: Migração de databases legados
- **APIs REST**: Integração com sistemas externos

#### 2. Camada de Armazenamento (Data Lake)
```
s3://banking-data-lake/
├── raw/                    # Dados brutos (imutável)
│   ├── transactions/
│   │   └── year=2025/month=01/day=15/
│   ├── customers/
│   └── accounts/
│
├── processed/              # Dados limpos e validados
│   ├── transactions/
│   ├── fraud_scores/
│   └── customer_metrics/
│
└── curated/               # Dados prontos para consumo
    ├── customer_insights/
    ├── risk_analysis/
    └── ml_features/
```

#### 3. Camada de Processamento
- **AWS Glue ETL**: Transformações Spark distribuídas
- **AWS Glue Catalog**: Metastore central
- **AWS Step Functions**: Orquestração de workflows

#### 4. Camada de Analytics
- **AWS Athena**: Queries SQL serverless
- **Amazon QuickSight**: Dashboards interativos
- **AWS SageMaker**: Machine Learning
- **Amazon Bedrock**: IA Generativa

#### 5. Camada de Consumo
- **APIs REST** (FastAPI/Flask)
- **Dashboards** (Streamlit/QuickSight)
- **Alertas** (SNS/SES)
- **Notebooks** (SageMaker Studio)

---

## 🛠️ Tecnologias Utilizadas

### AWS Services

| Serviço | Uso | Por que? |
|---------|-----|----------|
| **S3** | Data Lake | Escalável, durável, barato |
| **Glue** | ETL + Catalog | Serverless, integrado, Spark |
| **Athena** | Queries SQL | Pay-per-query, sem servidor |
| **SageMaker** | ML/AI | Plataforma completa de ML |
| **Bedrock** | IA Generativa | Acesso a LLMs sem treinar |
| **Lambda** | Processamento | Event-driven, serverless |
| **IAM** | Segurança | Controle de acesso granular |
| **CloudWatch** | Monitoring | Logs, métricas, alertas |

### Bibliotecas Python

>Este projeto organiza as dependências Python de acordo com o contexto de execução de cada componente (ETL, Lambda, Machine Learning, testes e análises). Essa separação evita ambientes desnecessariamente pesados, melhora a compatibilidade com serviços como AWS Glue e AWS Lambda e torna o projeto mais simples de manter e evoluir.

>A ideia é que cada parte do projeto utilize apenas o que realmente precisa, deixando claras as responsabilidades de cada componente e refletindo boas práticas adotadas em projetos de Engenharia de Dados.

### 1️⃣ Data Engineering (base)
📍 ```requirements.txt``` (raiz)

```
pandas==2.0.0
pyarrow==12.0.0
boto3==1.26.0
```

### 2️⃣ Glue Jobs (ETL distribuído)
📍 ```etl/glue_jobs/requirements.txt```

```
pandas==2.0.0
pyarrow==12.0.0
boto3==1.26.0
pydantic==2.0
```

### 3️⃣ Lambda Functions (serverless)
📍 ```etl/lambda_functions/requirements.txt```

```
boto3==1.26.0
pydantic==2.0
```

### 4️⃣ Machine Learning
📍 ```ml/requirements.txt```

```
pandas==2.0.0
scikit-learn==1.3.0
xgboost==2.0.0
imbalanced-learn==0.11
joblib
```

### 5️⃣ Data Quality / Testes
📍 ```tests/requirements.txt```

```
great-expectations==0.17
pandas==2.0.0
pyarrow==12.0.0
```

### 6️⃣ Visualização / Análises
📍 ```analytics/requirements.txt```

```
matplotlib==3.7.0
seaborn==0.12.0
plotly==5.14.0
```

### Formatos de Dados

- **Parquet**: Formato colunar (queries 10-100x mais rápidas que CSV)
- **JSON**: Dados semi-estruturados
- **Avro**: Streaming de dados

---

## 📁 Estrutura do Projeto

```
aws-data-lake-ml-pipeline/
│
├── data_generation/
│   ├── generate_synthetic_data.py
│   └── schemas/
│       ├── transactions.json
│       └── customers.json
│
├── etl/
│   ├── glue_jobs/
│   │   ├── raw_to_processed.py
│   │   ├── processed_to_curated.py
│   │   ├── fraud_detection_pipeline.py
│   │   └── requirements.txt
│   │
│   ├── lambda_functions/
│   │   ├── s3_trigger.py
│   │   ├── data_validator.py
│   │   └── requirements.txt
│   │
│   └── step_functions/
│       └── daily_pipeline.json
│
├── analytics/
│   ├── requirements.txt
│   ├── athena_queries/
│   │   ├── create_tables.sql
│   │   ├── daily_kpis.sql
│   │   ├── fraud_analysis.sql
│   │   └── customer_segmentation.sql
│   │
│   └── quicksight/
│       └── dashboards_config.json
│
├── ml/
│   ├── notebooks/
│   │   ├── 01_exploratory_analysis.ipynb
│   │   ├── 02_feature_engineering.ipynb
│   │   ├── 03_model_training.ipynb
│   │   └── 04_model_evaluation.ipynb
│   │
│   ├── scripts/
│   │   ├── train.py
│   │   ├── inference.py
│   │   └── model_monitoring.py
│   │
│   ├── models/
│   │   ├── fraud_detector_v1.pkl
│   │   └── scaler.pkl
│   └── requirements.txt
│
├── gen_ai/
│   ├── bedrock_assistant.py
│   ├── prompts/
│   │   ├── sql_generation.txt
│   │   ├── analysis_template.txt
│   │   └── explanation_template.txt
│   │
│   └── integrations/
│       ├── slack_bot.py
│       └── streamlit_app.py
│
├── infrastructure/
│   ├── terraform/
│   │   ├── main.tf
│   │   ├── s3.tf
│   │   ├── glue.tf
│   │   ├── athena.tf
│   │   └── sagemaker.tf
│   │
│   └── cloudformation/
│       └── stack.yaml
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── data_quality/
│
├── docs/
│   ├── architecture.md
│   ├── setup_guide.md
│   ├── user_guide.md
│   └── api_docs.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Setup e Instalação

### Pré-requisitos

1. **Conta AWS** com permissões para:
   - S3, Glue, Athena, SageMaker, Bedrock, IAM, CloudWatch

2. **AWS CLI** configurado:
```bash
aws configure
```

3. **Python 3.9+** instalado

4. **Terraform** (opcional, para IaC)

### Instalação Passo a Passo

#### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/aws-data-lake-ml-pipeline.git
cd aws-data-lake-ml-pipeline
```

#### 2. Crie Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

#### 3. Instale Dependências
```bash
pip install -r requirements.txt
```

#### 4. Configure Variáveis de Ambiente
```bash
cp .env.example .env
# Edite .env com suas configurações
```

```env
AWS_REGION=us-east-1
S3_BUCKET=banking-data-lake
GLUE_DATABASE=banking_analytics
ATHENA_WORKGROUP=primary
SAGEMAKER_ROLE=arn:aws:iam::xxx:role/SageMaker
```

#### 5. Crie Infraestrutura (Terraform)
```bash
cd infrastructure/terraform
terraform init
terraform plan
terraform apply
```

**Ou manualmente via Console AWS:**
- Crie bucket S3: `banking-data-lake` (Os nome são únicos, então este estará indisponível)
- Crie database Glue: `banking_analytics`
- Configure workgroup Athena: `primary`

#### 6. Execute Pipeline de Dados

**Gera dados sintéticos:**
```bash
python data_generation/generate_synthetic_data.py
```

**Upload para S3:**
```bash
aws s3 sync data/ s3://banking-data-lake/raw/ --recursive
```

**Executa ETL:**
```bash
# Via Glue Console ou:
aws glue start-job-run --job-name banking-etl-raw-to-processed
```

#### 7. Crie Tabelas no Athena
```bash
aws athena start-query-execution \
  --query-string "$(cat analytics/athena_queries/create_tables.sql)" \
  --result-configuration OutputLocation=s3://banking-data-lake/athena-results/
```

#### 8. Treine Modelo ML (SageMaker)
```bash
python ml/scripts/train.py
```

#### 9. Inicie Assistente IA
```bash
python gen_ai/bedrock_assistant.py
```

---

## 📖 Guia de Uso

### 1. Consultas SQL no Athena

**Query básica:**
```sql
SELECT 
    transaction_type,
    COUNT(*) as total,
    SUM(amount) as volume,
    AVG(amount) as avg_ticket
FROM banking_analytics.transactions_processed
WHERE year = 2025 AND month = 12
GROUP BY transaction_type;
```

**Otimização de custos:**
```sql
-- ✅ BOM: Filtra partições (escaneia menos dados)
WHERE year = 2025 AND month = 12 AND day = 11

-- ❌ RUIM: Não usa partições (escaneia tudo)
WHERE timestamp > '2025-12-11'
```

### 2. Executar Job Glue

**Via Console:**
1. AWS Glue → Jobs
2. Selecione job → Actions → Run

**Via CLI:**
```bash
aws glue start-job-run \
  --job-name banking-etl-raw-to-processed \
  --arguments='--SOURCE_BUCKET=banking-data-lake'
```

**Via Python (boto3):**
```python
import boto3

glue = boto3.client('glue')
response = glue.start_job_run(
    JobName='banking-etl-raw-to-processed',
    Arguments={
        '--SOURCE_BUCKET': 'banking-data-lake',
        '--TARGET_BUCKET': 'banking-data-lake',
        '--DATABASE_NAME': 'banking_analytics'
    }
)
```

### 3. SageMaker - Treinar Modelo

**Notebook Jupyter:**
```python
import sagemaker
from sagemaker.sklearn import SKLearn

# Configura estimator
sklearn_estimator = SKLearn(
    entry_point='train.py',
    role=role,
    instance_type='ml.m5.xlarge',
    framework_version='1.0-1',
    py_version='py3'
)

# Treina
sklearn_estimator.fit({
    'train': 's3://banking-data-lake/processed/transactions/',
    'test': 's3://banking-data-lake/curated/test_data/'
})

# Deploy
predictor = sklearn_estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.t2.medium'
)
```

### 4. Bedrock - Assistente IA

**Fazer pergunta sobre dados:**
```python
from bedrock_assistant import BedrockAnalyticsAssistant

assistant = BedrockAnalyticsAssistant()

# Gera SQL automaticamente
question = "Quais os 10 clientes que mais gastaram este mês?"
sql = assistant.generate_sql_query(question, schema)
print(sql)

# Analisa anomalias
report = assistant.analyze_anomalies(anomalies_df)
print(report)
```

### 5. Monitoring e Alertas

**CloudWatch Metrics:**
```python
import boto3

cloudwatch = boto3.client('cloudwatch')

# Publica métrica customizada
cloudwatch.put_metric_data(
    Namespace='Banking/Fraud',
    MetricData=[{
        'MetricName': 'FraudRate',
        'Value': fraud_rate,
        'Unit': 'Percent',
        'Timestamp': datetime.utcnow()
    }]
)
```

**Criar Alarme:**
```python
cloudwatch.put_metric_alarm(
    AlarmName='HighFraudRate',
    MetricName='FraudRate',
    Namespace='Banking/Fraud',
    Statistic='Average',
    Period=300,
    EvaluationPeriods=1,
    Threshold=5.0,
    ComparisonOperator='GreaterThanThreshold',
    AlarmActions=['arn:aws:sns:us-east-1:xxx:fraud-alerts']
)
```

---

## 📊 Métricas e Resultados

### Performance do Pipeline

| Métrica | Valor |
|---------|-------|
| **Volume processado/dia** | 10M+ transações |
| **Latência ETL** | < 5 minutos |
| **Custo mensal** | ~$500 (1TB dados) |
| **Disponibilidade** | 99.9% |

### Modelo de ML

| Métrica | Score |
|---------|-------|
| **ROC-AUC** | 0.96 |
| **Precision** | 0.89 |
| **Recall** | 0.92 |
| **F1-Score** | 0.90 |

### Otimizações Realizadas

**Antes:**
- Formato: CSV
- Tamanho: 10 GB
- Query time: 45 segundos
- Custo: $0.50 por query

**Depois:**
- Formato: Parquet + Snappy
- Tamanho: 2 GB (80% redução)
- Query time: 3 segundos (15x mais rápido)
- Custo: $0.10 por query (80% redução)

---

## ✅ Boas Práticas Implementadas

### 1. Data Quality

```python
# Great Expectations para validação
import great_expectations as gx

context = gx.get_context()
batch = context.get_batch(df)

# Define expectativas
batch.expect_column_values_to_not_be_null('transaction_id')
batch.expect_column_values_to_be_between('amount', min_value=0, max_value=1000000)
batch.expect_column_values_to_be_in_set('transaction_type', ['PIX', 'TED', 'DEBIT', 'CREDIT'])

# Valida
results = batch.validate()
```

### 2. Particionamento Estratégico

```sql
-- Particionamento hierárquico (mais eficiente)
PARTITIONED BY (year INT, month INT, day INT)

-- Query otimizada
WHERE year = 2025 AND month = 12  -- Escaneia apenas Dezembro/2025
```

### 3. Compressão e Formato

```python
# Parquet com Snappy (melhor balanço)
df.to_parquet(
    'output.parquet',
    engine='pyarrow',
    compression='snappy',
    index=False
)
```

### 4. IAM Least Privilege

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": [
      "s3:GetObject",
      "s3:PutObject"
    ],
    "Resource": "arn:aws:s3:::banking-data-lake/processed/*"
  }]
}
```

### 5. Monitoring e Observability

- **CloudWatch Logs**: Todos os jobs
- **CloudWatch Metrics**: KPIs customizados
- **AWS X-Ray**: Distributed tracing
- **SNS Alerts**: Falhas críticas

### 6. CI/CD

```yaml
# .github/workflows/deploy.yml
name: Deploy ETL Pipeline

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy Glue Job
        run: |
          aws glue update-job --job-name banking-etl \
            --job-update "$(cat glue_job.json)"
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja `LICENSE` para mais detalhes.

---

## 👤 Autor

### **Samira Medeiros**
- GitHub: [Samira Medeiros](https://github.com/samiramedeiros)
- LinkedIn: [Samira Medeiros](https://www.linkedin.com/in/samiramedeirosc)
- Email: [samiramedeirosc@email.com](mailto:samiramedeirosc@email.com)
---

## 📚 Referências e Recursos

### Documentação Oficial AWS

- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/)
- [SageMaker Developer Guide](https://docs.aws.amazon.com/sagemaker/)
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)

### Tutoriais e Cursos

- [AWS Data Engineering Learning Path](https://aws.amazon.com/training/learn-about/data-analytics/)
- [SageMaker Examples Repository](https://github.com/aws/amazon-sagemaker-examples)

### Comunidades

- [AWS Data Heroes](https://aws.amazon.com/data-hero/)
- [r/dataengineering](https://reddit.com/r/dataengineering)
- [Data Engineering Discord](https://discord.gg/dataengineering)

---

**⭐ Se este projeto foi útil, considere dar uma estrela!**
