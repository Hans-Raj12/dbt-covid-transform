with silver as (
    select * from {{ref('silver_covid_data')}}
)

select
    country,
    total_cases,
    total_deaths,
    total_recovered,
    active_cases,
    "death_rate_%",
    "recovery_rate_%"

from silver
order by total_cases desc
limit 20