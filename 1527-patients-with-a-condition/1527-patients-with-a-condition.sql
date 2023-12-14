# Write your MySQL query statement below


select *
from Patients p
where p.conditions regexp '\\bDIAB1'