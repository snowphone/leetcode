# Write your MySQL query statement below



SELECT 
    p.project_id,
    coalesce(
        round(
            avg(
                e.experience_years
            ),
            2
        ),
        0
    ) as average_years
FROM Project AS p
LEFT OUTER JOIN Employee AS e on p.employee_id = e.employee_id
GROUP BY p.project_id