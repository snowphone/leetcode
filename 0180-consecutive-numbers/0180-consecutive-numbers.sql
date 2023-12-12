# Write your MySQL query statement below

select distinct l.num as ConsecutiveNums
from Logs as l
where l.num = (
    select m.num from Logs m where m.id = l.id + 1
) and l.num = (
    select n.num from Logs n where n.id = l.id + 2
)