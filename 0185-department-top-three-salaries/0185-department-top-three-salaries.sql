-- Write your PostgreSQL query statement below

select
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
from Department d
join Employee e on d.id = e.departmentId
    and e.salary in (
        select distinct e2.salary
        from Employee e2
        where e2.departmentId = d.id
        order by e2.salary desc
        limit 3
    )
