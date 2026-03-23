CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
  SET M = N - 1;

  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT salary 
      FROM Employee
      ORDER BY salary DESC
      -- 2. Use the variable instead of the expression
      LIMIT M, 1
  );
END