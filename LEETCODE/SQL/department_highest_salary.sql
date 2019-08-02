SELECT Department.Name AS Department, T1.Name AS Employee, T1.Salary
FROM Employee AS T1
        JOIN (SELECT DepartmentId, MAX(Salary) AS MAXSalary
                FROM Employee
                GROUP BY DepartmentId) AS T2
            ON T1.DepartmentId = T2.DepartmentId
        JOIN Department
            ON T1.DepartmentId = Department.Id
    WHERE T1.Salary = T2.MAXSalary;