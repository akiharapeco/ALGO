SELECT T1.Name AS Customers
    FROM Customers AS T1
    WHERE T1.Id NOT IN (SELECT CustomerId
                            FROM Orders);