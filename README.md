# 🏗️ dbt COVID-19 Data Transform

A dbt (Data Build Tool) project that transforms raw COVID-19 data following the Medallion Architecture (Bronze -> Silver -> Gold) using PostgreSQL. This project builds on top of the ELT pipeline project and demonstrates professional data modelling and transformation skills.

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

- **dbt** - Data transformation and modelling
- **PostgreSQL** - Relational Database
- **SQL** - Core transformation language 
- **YAML** - Model documentation and testing

---

## 📁 Project Structure

| File/Folder | Description |
|---|---|
| `models/bronze/` | Raw layer — reads data as is from PostgreSQL |
| `models/silver/` | Cleaning layer — filters and validates data |
| `models/gold/` | Business layer — aggregated, analytics-ready models |
| `models/schema.yml` | Model documentation and data tests |
| `dbt_project.yml` | dbt project configuration |


---

## ⚙️ How to Run This Project

**1. Clone the repository**
```bash
git clone https://github.com/Hans-Raj12/dbt-covid-transform.git
cd dbt-covid-transform
```

**2. Install dbt**
```bash
pip3 install dbt-postgres
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

**4. Run the models**
```bash
dbt run
```

**5. Run the tests**
```bash
dbt test
```

---

## 📊 Data Models Overview

**Bronze - Raw Layer**
Reads raw COVID-19 data directly from PostgreSQL as loaded by the ETL pipeline.

**Silver - Cleaning**
Filters out countries with zero cases, zero population, and zero test to ensure only meaningful data flows into the gold layer.

**Gold- Business Layer**
Three business ready models answering real analytical questions:
- which countries were most affected?
- which countries had the highest death rates?
- which countries had the best testing coverage?

---

## 🔗 Related Project

This project builds on top of the ETL pipeline that extracts and loads the raw data:
👉 [ETL COVID-19 Pipeline](https://github.com/Hans-Raj12/etl-covid-pipeline)


---

## 👨‍💻 Author

**Hans Raaj**

Transitioning from FullStack Development into Data Engineering. Open to Data Engineer, ETL Developer, and Data Analyst roles.

[GitHub](https://github.com/Hans-Raj12) | [LinkedIn](https://www.linkedin.com/in/hans-raaj/)