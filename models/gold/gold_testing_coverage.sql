with silver as (
    select * from {{ ref("silver_covid_data")}}
)

select
    country,
    total_tests,
    population,
    tests_per_million,
    "recovery_rate_%"

from silver
order by tests_per_million desc
limit 20 