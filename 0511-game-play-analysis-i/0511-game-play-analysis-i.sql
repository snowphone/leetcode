# Write your MySQL query statement below

select a.player_id, min(a.event_date) as first_login
from Activity as a
group by a.player_id