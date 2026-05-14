with silver as (
    select * from {{ ref("silver_covid_data")}}
)

select
    country,
    total_cases,
    total_deaths,
    "death_rate_%",
    population
from silver
where total_cases > 10000
order by "death_rate_%" desc
limit 20
