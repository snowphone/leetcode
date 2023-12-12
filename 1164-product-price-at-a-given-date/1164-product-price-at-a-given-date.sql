# Write your MySQL query statement below

with cte as (
    select p.product_id, max(p.change_date) as change_date
    from Products p
    where p.change_date <= '2019-08-16'
    group by p.product_id
)
(
    select c.product_id, p.new_price as price
    from cte c
    join Products p on c.product_id = p.product_id and c.change_date = p.change_date
) union (
    select distinct p.product_id, 10 as price
    from Products p
    where p.product_id not in (select p.product_id from cte p)
)