# Write your MySQL query statement below

(
    select u.name as results
    from MovieRating mr
    join Users u on u.user_id = mr.user_id
    group by u.user_id, u.name
    order by count(mr.rating) desc, u.name asc
    limit 1
)
union all
(
    select m.title as results
    from MovieRating mr
    join Movies m on m.movie_id = mr.movie_id
    where mr.created_at between '2020-02-01' and '2020-02-29'
    group by mr.movie_id
    order by avg(mr.rating) desc, m.title asc
    limit 1
)
