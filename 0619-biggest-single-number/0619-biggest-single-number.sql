# Write your MySQL query statement below

with singles as (
    select n.num
    from MyNumbers n
    group by n.num
    having count(*) = 1
)
select max(num) as num
from singles
