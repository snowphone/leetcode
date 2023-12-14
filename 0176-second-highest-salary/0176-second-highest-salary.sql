# Write your MySQL query statement below

select max(e.salary) as SecondHighestSalary
from Employee e
where e.salary < (select max(e2.salary) from Employee e2)