SELECT 
    v.customer_id, 
    COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
WHERE NOT EXISTS (
    SELECT 1 
    FROM Transactions AS t 
    WHERE t.visit_id = v.visit_id
)
GROUP BY v.customer_id;