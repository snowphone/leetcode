# Write your MySQL query statement below

(
    select e.employee_id, e.department_id
    from Employee as e
    where e.primary_flag = 'Y'
) union (
    select e.employee_id, min(e.department_id)
    from Employee as e
    group by e.employee_id
    having count(*) = 1
)
