# 🏗️ dbt COVID-19 Data Transform

ETL pipeline that extracts live COVID-19 data, transforms it using Python & Pandas, loads it into PostgreSQL, models it with dbt following Medallion Architecture, and orchestrates everything with Apache Airflow.

---

## 🏛️ Pipeline Architecture
API (disease.sh) → Extract → Transform → Load → dbt Models → Dashboard
↑
Orchestrated by Airflow (runs daily)
---


## 🏅 Medallion Architecture
| Layer | Model | Description |
|---|---|---|
| 🥉 Bronze | `bronze_covid_data` | Raw data read directly from PostgreSQL |
| 🥈 Silver | `silver_covid_data` | Cleaned and filtered data, nulls removed |
| 🥇 Gold | `gold_top_affected_countries` | Top 20 most affected countries by total cases |
| 🥇 Gold | `gold_highest_death_rate` | Top 20 countries with highest death rate |
| 🥇 Gold | `gold_testing_coverage` | Top 20 countries by testing coverage per million |

---

## 🛠️ Tools & Technologies

- **Python** - Core programming language
- **Pandas** - Data transformation and manipulation
- **SQLAlchemy** - Database connection and ORM
- **dbt** - Data transformation and modelling
- **PostgreSQL** - Relational Database
- **Apache Airflow** - Pipeline orchestration and scheduling
- **Google Data Studio** - Interactive dashboard and visualization
- **Requests** - API data extraction
- **dotenv** - Secure environment variable management
---

## 📁 Project Structure

| File/Folder | Description |
|---|---|
| `dags/covid_etl_dag.py` | Airflow DAG that orchestrates the full pipeline daily |
| `models/bronze/` | Raw layer — reads data as is from PostgreSQL |
| `models/silver/` | Cleaning layer — filters and validates data |
| `models/gold/` | Business layer — aggregated, analytics-ready models |
| `models/schema.yml` | Model documentation and data tests |
| `dbt_project.yml` | dbt project configuration |

---

## 🔄 Pipeline Stages

| Stage | Tool | Description |
|---|---|---|
| **Extract** | Python, Requests | Pulls live COVID-19 data from disease.sh API across 229 countries |
| **Transform** | Python, Pandas | Cleans data and engineers metrics like death rate and recovery rate |
| **Load** | SQLAlchemy, PostgreSQL | Stores structured data into PostgreSQL |
| **Model** | dbt | Transforms data through Bronze → Silver → Gold layers |
| **Orchestrate** | Apache Airflow | Runs the full pipeline automatically every day |
| **Visualize** | Looker Studio | Interactive dashboard built on Gold layer models |

---

## ⚙️ How to Run This Project

**1. Clone the repository**
```bash
git clone https://github.com/Hans-Raj12/dbt-covid-transform.git
cd dbt-covid-transform
```

**2. Install dbt**
```bash
pip3 install pandas requests sqlalchemy psycopg2-binary python-dotenv dbt-postgres apache-airflow
```

**3. Set up your profiles.yml at ~/.dbt/profiles.yml**
```yaml
dbt_covid_transform:
    target: dev
    outputs:
    dev:
        type: postgres
        host: localhost
        port: 5432
        user: your_username
        password: ""
        dbname: covid_etl
        schema: public
        threads: 1
```

**4. Copy the DAG to Airflow**
```bash
cp dags/covid_etl_dag.py ~/airflow/dags/
```

**5. Start Airflow and trigger the pipeline**
```bash
airflow standalone
```


Then open `http://localhost:8080` and trigger the `covid_etl_pipeline` DAG.

---

## 📊 Live Dashboard

👉 [COVID-19 Global Data Dashboard](
https://datastudio.google.com/reporting/bc2ab8f9-f217-45f3-bc5c-c223f775e236

) — Built on dbt Gold layer models using Google Looker Studio


---

## 🔗 Related Project

This project builds on top of the ETL pipeline that extracts and loads the raw data:
👉 [ETL COVID-19 Pipeline](https://github.com/Hans-Raj12/etl-covid-pipeline)


---

## 👨‍💻 Author

**Hans Raaj**

Transitioning from FullStack Development into Data Engineering. Open to Data Engineer, ETL Developer, and Data Analyst roles.

[GitHub](https://github.com/Hans-Raj12) | [LinkedIn](https://www.linkedin.com/in/hans-raaj/)