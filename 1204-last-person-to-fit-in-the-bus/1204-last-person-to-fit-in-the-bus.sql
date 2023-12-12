# Write your MySQL query statement below

with last_turn as (
    select max(q.turn) as turn
    from Queue q
    where 1000 >= (
        select sum(r.weight)
        from Queue r
        where r.turn <= q.turn
    )
)
select q.person_name
from Queue q
where q.turn = (select * from last_turn)