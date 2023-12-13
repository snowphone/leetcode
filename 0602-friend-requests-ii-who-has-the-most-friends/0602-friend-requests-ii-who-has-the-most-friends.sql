# Write your MySQL query statement below

with ids as (
    select ra.requester_id as id
    from RequestAccepted ra
    union all
    select ra.accepter_id as id
    from RequestAccepted ra
)
select i.id, count(*) as num
from ids as i
group by i.id
order by count(*) desc
limit 1