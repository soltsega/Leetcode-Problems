# Write your MySQL query statement below
SELECT email FROM (
SELECT email, COUNT(*) AS occurrenceCount
FROM Person
GROUP BY email
) AS tempTable
WHERE occurrenceCount > 1;
