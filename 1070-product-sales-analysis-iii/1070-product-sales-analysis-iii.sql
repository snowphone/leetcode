# Write your MySQL query statement below

with first_year as (
    select s.product_id, min(year) as year
    from Sales s
    group by s.product_id
)
select s.product_id, s.year as first_year, s.quantity, s.price
from Sales s
join first_year f on s.product_id = f.product_id and s.year = f.year