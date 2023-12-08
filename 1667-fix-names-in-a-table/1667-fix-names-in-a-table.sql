# Write your MySQL query statement below

-- Note that SQL is 1-indexed
select 
    u.user_id,
    CONCAT(
        UPPER(SUBSTR(u.name, 1, 1)),
        LOWER(SUBSTR(u.name, 2))
    ) as name
from
    Users as u
order by u.user_id