# Write your MySQL query statement below

select *
from Users as u
where u.mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$'