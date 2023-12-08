# Write your MySQL query statement below

select t.tweet_id
from Tweets as t
where LENGTH(t.content) > 15