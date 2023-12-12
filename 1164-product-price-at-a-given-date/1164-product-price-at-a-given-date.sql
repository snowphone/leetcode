# Write your MySQL query statement below

select p.product_id, 10 as price
from Products p
where p.product_id not in (
    select q.product_id
    from Products q
    where q.change_date <= '2019-08-16'
)

union

select p.product_id, p.new_price as price
from Products p
where (p.product_id, p.change_date) in (
    select q.product_id, max(q.change_date) as change_date
    from Products q
    where q.change_date <= '2019-08-16'
    group by q.product_id
)