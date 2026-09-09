# Write your MySQL query statement below
select d.name as Department, e.name as Employee, e.salary as Salary
from Employee e
join Department d on e.departmentid = d.id 
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM Employee e2
    WHERE e.departmentId = e2.departmentId
);
