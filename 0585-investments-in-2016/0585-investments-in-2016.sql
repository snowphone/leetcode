# Write your MySQL query statement below

with uniques as (
    select 
        min(i.pid) as pid,
        min(i.lat) as lat,
        min(i.lon) as lon
    from Insurance i
    group by i.tiv_2015
    having count(*) = 1
),
joined as (
    select i.pid
    from Insurance i
    join uniques u
        on i.pid != u.pid
        and i.lat = u.lat
        and i.lon = u.lon
)
select round(sum(i.tiv_2016), 2) as tiv_2016
from Insurance i
where i.pid not in (
    select pid from uniques
    union all
    select pid from joined
) and not exists (
    select *
    from Insurance j
    where i.pid != j.pid
    and i.lat = j.lat
    and i.lon = j.lon
)