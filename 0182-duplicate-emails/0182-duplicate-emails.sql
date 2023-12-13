# Write your MySQL query statement below

select distinct p.email
from Person p
group by p.email
having count(*) > 1