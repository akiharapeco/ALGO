/* Write your T-SQL query statement below */
SELECT Salary
    From (SELECT Salary, RANK () OVER (ORDER BY Salary) AS rank 
            FROM Employee
         ) AS T
    WHERE T.rank = 2;