# Write your MySQL query statement below

-- Unfortunately, delete query with cte is not possible
delete
from Person as p
where p.id not in (
    select *
    from (
        select min(id)
        from Person
        group by email
    ) _
)