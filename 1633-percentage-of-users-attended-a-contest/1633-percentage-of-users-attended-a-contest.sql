# Write your MySQL query statement below

WITH cnt_table AS (
    SELECT 
        r.contest_id,
        COUNT(r.contest_id) AS cnt
    FROM Users AS u
    LEFT OUTER JOIN Register AS r ON u.user_id = r.user_id
    GROUP BY r.contest_id
), user_cnt AS (
    SELECT CAST( COUNT(*) AS DECIMAL) AS cnt
    FROM Users
)

SELECT 
    r.contest_id,
    ROUND(
        c.cnt / u.cnt * 100,
        2
    ) AS percentage
FROM Register AS r
LEFT OUTER JOIN cnt_table AS c on r.contest_id = c.contest_id
CROSS JOIN user_cnt AS u
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC

