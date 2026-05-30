# Write your MySQL query statement 
-- Technique used: 
select name
from Employee 
where id in (
    select managerId
    from Employee
    group by managerId
    having count(managerId)>=5
)

