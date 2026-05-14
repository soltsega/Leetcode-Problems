-- Overall time complexity: O(N*K) where N is the number of rows and K is the lenght of each string 
-- Overall space complexity: O(N*K) where N and K as in the above


# Write your MySQL query statement below
select user_id, concat(upper(left(name, 1)), lower(substring(name, 2))) 
as name 
from Users
order by user_id;