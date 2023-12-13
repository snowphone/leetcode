# Write your MySQL query statement below

with dates as (
    select distinct visited_on as date
    from Customer
    order by visited_on
)
select
    d.date as visited_on,
    sum(c.amount) as amount,
    round( sum(c.amount) / 7., 2) as average_amount
from dates d
join Customer c on c.visited_on between d.date - interval 6 day and d.date
group by d.date
having count(distinct c.visited_on) = 7
order by d.date