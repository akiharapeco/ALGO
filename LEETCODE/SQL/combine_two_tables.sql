# Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State 
    FROM Person AS P LEFT OUTER JOIN Address AS A
        ON P.PersonId = A.PersonId;