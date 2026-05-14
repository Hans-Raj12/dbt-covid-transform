with bronze as (
    select * from {{ref('bronze_covid_data')}}
),

cleaned as (
    select 
        country,
        total_cases,
        total_deaths,
        total_recovered,
        active_cases,
        critical_cases,
        total_tests,
        population,
        "death_rate_%",
        "recovery_rate_%",
        tests_per_million

    from bronze

    -- Remove countries with no meaningful data
    where total_cases > 0
        and population > 0
        and total_tests > 0

)

select * from cleaned