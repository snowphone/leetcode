# Write your MySQL query statement below

with tbl as (
    select 
    substr(
        cast(t.trans_date as char), 1, 7
    ) as month,
        t.country,
        t.state,
        t.amount
    from Transactions t
), total as (
    select t.month, t.country, count(*) as cnt, sum(t.amount) as amount
    from tbl as t
    group by t.month, t.country
), appr as (
    select t.month, t.country, count(*) as cnt, sum(t.amount) as amount
    from tbl as t
    where t.state = 'approved'
    group by t.month, t.country
)
select
    t.month,
    t.country,
    t.cnt as trans_count,
    coalesce(a.cnt, 0) as approved_count,
    t.amount as trans_total_amount,
    coalesce(a.amount, 0) as approved_total_amount
from total as t
left outer join appr as a on
    t.month = a.month and (
        t.country = a.country or 
        (t.country is null and a.country is null )
    )