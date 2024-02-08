-- Write your PostgreSQL query statement below

with cnt as (
    select o.customer_number, count(*) as cnt
    from Orders as o
    group by o.customer_number
)
select c.customer_number
from cnt as c
order by c.cnt desc
limit 1