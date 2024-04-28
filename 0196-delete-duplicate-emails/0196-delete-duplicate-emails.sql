# Write your MySQL query statement below
Delete p from Person p, Person p2
where p.id > p2.id and p.email = p2.email