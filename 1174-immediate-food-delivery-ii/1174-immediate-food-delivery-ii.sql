# Write your MySQL query statement below


with FirstOrder as (
    select 
        d.customer_id,
        min(d.order_date) as order_date
    from Delivery d
    group by d.customer_id
), type_table as (
    select 
        d.order_date = d.customer_pref_delivery_date as immediated
    from Delivery d
    join FirstOrder f on d.customer_id = f.customer_id and d.order_date = f.order_date
    group by d.customer_id
)
select  round( sum(d.immediated) / count(*) * 100. , 2 ) as immediate_percentage
from type_table d

