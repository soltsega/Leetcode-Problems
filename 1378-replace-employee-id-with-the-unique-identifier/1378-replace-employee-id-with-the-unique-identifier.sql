/* Write your T-SQL query statement below */
-- Technique used: Left join
SELECT 
    eu.unique_id, 
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu 
    ON e.id = eu.id;