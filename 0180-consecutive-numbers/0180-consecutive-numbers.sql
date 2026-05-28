# Write your MySQL query statement below
-- the things i have learnt today
-- with is used to create a named temporary table
-- lead() is a method that is used to select a specific records next, nextnext or nth record from now
-- over - acts as a window that the operator acts on
with ranked as (
    select 
    num,
    lead(num,1) over (order by id) as next,
    lead(num,2) over (order by id) as nextnext
    from Logs
)

select distinct num as  ConsecutiveNums 
from ranked
where num = next and num=nextnext