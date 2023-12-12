# Write your MySQL query statement below

select 
    t.x,
    t.y,
    t.z,
    case
        when greatest(t.x, t.y, t.z) * 2 < t.x + t.y + t.z then 'Yes'
        else 'No'
    end as triangle
from triangle t