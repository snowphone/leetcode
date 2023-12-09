# Write your MySQL query statement below

select m.name
from Employee as m
join Employee as e on m.id = e.managerId
group by m.id
having count(*) >= 5
