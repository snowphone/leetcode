# Write your MySQL query statement below

select distinct l.num as ConsecutiveNums
from Logs as l
join Logs m on l.id + 1 = m.id and l.num = m.num
join Logs n on l.id + 2 = n.id and l.num = n.num