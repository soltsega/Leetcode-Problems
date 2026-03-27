-- Write your PostgreSQL query statement below
-- Techniques used: Subquery, GROUP BY, HAVING, COUNT, and MAX
SELECT MAX(num) as num
FROM (
    SELECT num 
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
);