# Write your MySQL query statement below

SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary
FROM Department d
JOIN Employee e ON d.id = e.departmentId
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = d.id AND e2.salary >= e.salary
) <= 3;