# Write your MySQL query statement below

with cte as (
    select 
        a.id, coalesce(b.student, a.student) as student
    from Seat a
    left outer join Seat b on a.id + 1 = b.id
    where a.id % 2 = 1
    
    union
    
    select 
        b.id, a.student
    from Seat b
    left outer join Seat a on a.id + 1 = b.id
    where b.id % 2 = 0
)
select *
from cte
order by id