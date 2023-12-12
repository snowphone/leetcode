# Write your MySQL query statement below

select q.person_name
from Queue q
where 1000 >= (
    select sum(r.weight)
    from Queue r
    where r.turn <= q.turn
)
order by q.turn desc
limit 1
