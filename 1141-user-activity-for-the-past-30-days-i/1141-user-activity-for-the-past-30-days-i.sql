# Write your MySQL query statement below


select a.activity_date as day, count(distinct a.user_id) as active_users
from Activity a
where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
group by a.activity_date
having count(distinct a.user_id) > 0