# Write your MySQL query statement below

with first_time as (
    select a.player_id, min(event_date) as date
    from Activity a
    group by a.player_id
)
select round(
    count(distinct f.player_id) / (select count(distinct player_id) from Activity),
    2
) as fraction
from first_time f
join Activity a2 on f.player_id = a2.player_id and DATEDIFF(a2.event_date, f.date) = 1