# Write your MySQL query statement below

select
    m.employee_id,
    m.name,
    count(*) as reports_count,
    round(avg(e.age)) as average_age
from Employees m
join Employees e on e.reports_to = m.employee_id
group by m.employee_id, m.name
having count(*) > 0
order by m.employee_id