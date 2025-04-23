WITH RankedSalaries AS (
    SELECT e.name AS Employee,
           d.name AS Department,
           e.salary AS Salary,
           DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS `rank`
    FROM Employee e
    JOIN Department d ON e.departmentId = d.id
)
SELECT Employee, Department, Salary
FROM RankedSalaries
WHERE `rank` <= 3;