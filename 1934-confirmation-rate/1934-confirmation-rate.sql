# Write your MySQL query statement below

with 
    confirmed as (
        select 
            s.user_id,
            cast( count(c.time_stamp) as decimal) as cnt
        from Signups s
        left join Confirmations c on s.user_id = c.user_id and c.action = 'confirmed'
        group by s.user_id
    ),
    all_table as (
        select 
            s.user_id,
            cast( count(c.time_stamp) as decimal) as cnt
        from Signups s
        left join Confirmations c on s.user_id = c.user_id
        group by s.user_id
    )
select 
    c.user_id, 
    case when c.cnt > 0 then
        round(c.cnt / a.cnt, 2)
    else
        0
    end as confirmation_rate
from confirmed as c
join all_table as a on c.user_id = a.user_id
