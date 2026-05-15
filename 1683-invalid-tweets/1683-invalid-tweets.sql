# Write your MySQL query statement below
-- Time complexity: O(N) where 
-- Space complexity: O(N)

select tweet_id
from Tweets
where length(content) > 15