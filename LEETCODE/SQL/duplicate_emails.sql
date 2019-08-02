SELECT Email
    FROM Person AS T1
    GROUP BY Email
    HAVING COUNT(Id) > 1;