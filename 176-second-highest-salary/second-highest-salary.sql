# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT DISTINCT salary
    FROM Employee
) AS t
WHERE salary < (SELECT MAX(salary) FROM Employee);