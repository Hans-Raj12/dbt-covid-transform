import psycopg2
import pandas as pd

# connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="covid_etl",
    user="hansraaj"
)

# export gold layer models
print("⏳ Exporting Gold layer data...")

# top affected countries
df1 = pd.read_sql("SELECT * FROM gold_top_affected_countries",conn)
df1.to_csv("gold_top_affected_countries.csv", index=False)
print(f"Exported top affected countries - {len(df1)} rows")

# highest death rate
df2 = pd.read_sql('SELECT * FROM gold_highest_death_rate',conn)
df2.to_csv("gold_highest_death_rate.csv",index=False)
print(f"Exported highest death rate - {len(df2)} rows")

#Testing coverage
df3 = pd.read_sql("SELECT * FROM gold_testing_coverage",conn)
df3.to_csv("gold_testing_coverage.csv",index=False)
print(f"Exported testing coverage - {len(df3)} rows")

conn.close()
print("🎉 All Gold layer data exported successfully")