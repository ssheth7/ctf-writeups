## Challenge 1
#### Here you are given another SQL injection challenge. The description says that the users table is protected, meaning it isn't. Let's try the solution to the previous challenge:
> ' or '1' = '1
#### This input dumps the contents of the current table, but not the users table. Luckily, the UNION SELECT query can be used to access other tables in the database. So lets try
> 'UNION SELECT * FROM users'
####Syntax error. OK, maybe there's a filter we have to bypass. Since our first query dumped the table, we can assume that single quotes aren't filtered.
Solution: So lets try
> ' uNion sElect * from users'
and success! The next flag is in the users table.