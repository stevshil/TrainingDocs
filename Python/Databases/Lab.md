# Python Database Lab

In this mini-lab we want you to use Python to create and use a database.

# Part 1

Create a Python script that can be used to create a new database and schema.

1. The database should be called **MyPasswords**.
2. Create a table called **Passwords** with the following fields;
    - Name
    - LoginID
    - Password
    - URL (NULL)
    - Notes (Null)
    - DeletedDate (Null)
    - CreationDate
    - ModificationDate (Null)
3. Create another table called **Certificates** with the following fields;
    - Name
    - ServerName
    - Certificate
    - Notes (Null)
    - DeletedDate (Null)
    - CreationDate
    - ModificationDate (Null)
4. Insert some data into each of the tables, 3 to 5 records will be enough.
    * Make sure you use Python to perform the population.
    * Add 1 record into either table where the DeletedDate is 10 years ago.

# Part 2

Write a separate Python script that will test your database to ensure that;

1. It finds 1 record in each table.
2. Can insert a record into each table.  Make sure that the insert sets the CreationDate to the current date and time now.
3. Updates a specific record in each table, and changes the ModificationDate to the time and date of update.
4. Delete a record by inserting a date time into the rows DeletedDate field - do not delete the actual record.
5. Have a purge function that will actually delete any data that is more than 7 years old.