# Write your MySQL query statement below

select round(sum(i.tiv_2016), 2) as tiv_2016
from Insurance i
where (i.lat, i.lon) not in (
    select j.lat, j.lon
    from Insurance j
    where i.pid != j.pid
) and i.tiv_2015 in (
    select j.tiv_2015
    from Insurance j
    where i.pid != j.pid 
)
