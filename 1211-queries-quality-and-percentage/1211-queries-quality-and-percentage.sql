# Write your MySQL query statement below

with tmp as (
    select 
        q.query_name,
        q.rating,
        q.rating * 1. / q.position as quality
    from Queries as q
)
select 
    q.query_name,
    round(
        avg(q.quality),
        2
    ) as quality,
    round(
        (
            select count(*)
            from tmp
            where tmp.rating < 3 and tmp.query_name = q.query_name
        )
        * 100. 
        / (
            select count(*)
            from tmp
            where tmp.query_name = q.query_name
        ),
        2
    ) as poor_query_percentage
from tmp as q
where q.query_name is not null
group by q.query_name