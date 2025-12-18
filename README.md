# 🏦 Banking Data Lake & Analytics Pipeline (AWS)

### 📌 Visão Geral

Este projeto implementa um **pipeline completo de Engenharia de Dados na AWS**, simulando um cenário real do setor bancário.  
O foco está na **construção de um Data Lake bem estruturado**, com camadas bem definidas, automação via **AWS Step Functions** e consumo analítico via **Amazon Athena**.

O projeto foi pensado como um **case profissional**, priorizando boas práticas de arquitetura, clareza de responsabilidades entre camadas e governança de dados.

---

### 🎯 Objetivos do Projeto

- Construir um **Data Lake na AWS** seguindo o padrão:
  - **Raw → Processed → Curated**
- Processar dados transacionais bancários com **AWS Glue (Spark)**
- Gerar **datasets analíticos prontos para negócio e ML**
- Orquestrar todo o fluxo com **AWS Step Functions**
- Disponibilizar os dados finais para consulta via **Amazon Athena**

---

### 🧱 Arquitetura do Data Lake

### 📂 Camadas

### 🔹 Raw/Bronze
- Dados brutos de transações bancárias
- Sem tratamento
- Armazenados no Amazon S3

### 🔹 Processed/Silver
- Dados limpos e padronizados
- Tipos ajustados, colunas normalizadas
- Prontos para agregações e regras de negócio

### 🔹 Curated/Gold (Camada Analítica)
A camada **Curated NÃO contém dados transacionais crus**.  
Ela é composta apenas por **datasets analíticos e métricas**, como:

- `customer_insights` → métricas por cliente
- `risk_analysis` → indicadores de risco
- `ml_features` → features prontas para Machine Learning

> O curated layer é voltado para consumo analítico e modelos. Transações cruas ficam no processed para evitar duplicação e custos desnecessários. 

---

### 🔄 Fluxo do Pipeline

1. **Raw → Processed**
   - Job Glue: `raw_to_processed.py`
   - Limpeza e padronização dos dados

2. **Processed → Curated**
   - Job Glue: `processed_to_curated.py`
   - Geração de métricas por cliente

3. **Processed → Risk Analysis**
   - Job Glue: `processed_to_risk_analysis.py`
   - Criação de indicadores de risco

4. **Processed → ML Features**
   - Job Glue: `processed_to_ml_features.py`
   - Geração de features prontas para modelos

5. **Orquestração**
   - AWS Step Functions coordena toda a execução diária

6. **Consumo**
   - Amazon Athena consulta os dados curados

---

### ⏩ AWS Step Functions

<img width="519" height="495" alt="step-functions" src="https://github.com/user-attachments/assets/5539f398-64a2-4eae-850c-1f759d957564" />


---

### 🧠 Onde entra Machine Learning?

Este projeto **não treina modelos de Machine Learning propositalmente**.

### ✔️ Decisão arquitetural consciente 

O papel da Engenharia de Dados neste contexto é:

- Garantir **dados confiáveis**
- Criar **features reutilizáveis**
- Preparar dados para **cientistas de dados ou pipelines de ML**

O dataset `ml_features` representa exatamente o **contrato entre Engenharia de Dados e Machine Learning**.

> Em ambientes reais, o treinamento de modelos ocorre em pipelines separados (ex: SageMaker), consumindo essas features.

---

### 🧰 Tecnologias Utilizadas

- **AWS S3** — Data Lake
- **AWS Glue (Spark)** — Processamento de dados
- **AWS Step Functions** — Orquestração
- **Amazon Athena** — Consultas analíticas
- **Python / PySpark**
- **Apache Parquet**

---

### 📁 Estrutura do Repositório

```text
aws-data-lake-ml-pipeline/
├── etl/
│   ├── glue_jobs/
│   │   ├── raw_to_processed.py
│   │   ├── processed_to_curated.py
│   │   ├── processed_to_risk_analysis.py
│   │   └── processed_to_ml_features.py
│   └── step_functions/
│       └── daily_pipeline.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

### 📊 Exemplos de Uso (Athena)
```
SELECT COUNT(*) FROM banking_db.customer_insights;
SELECT COUNT(*) FROM banking_db.risk_analysis;
SELECT COUNT(*) FROM banking_db.ml_features;
```

---

### 🚀 Conclusão

Este projeto demonstra:

- Arquitetura de Data Lake madura

- Separação clara de responsabilidades

- Boas práticas de Engenharia de Dados

- Visão realista de como ML se integra ao pipeline

- Automação e escalabilidade na AWS

---

### 📄 Licença

Este projeto está sob a licença MIT. Veja `LICENSE` para mais detalhes.

---

### 👤 Autor

### **Samira Medeiros**
- GitHub: [Samira Medeiros](https://github.com/samiramedeiros)
- LinkedIn: [Samira Medeiros](https://www.linkedin.com/in/samiramedeirosc)
- Email: [samiramedeirosc@email.com](mailto:samiramedeirosc@email.com)
