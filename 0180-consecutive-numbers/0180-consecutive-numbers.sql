# Write your MySQL query statement below
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