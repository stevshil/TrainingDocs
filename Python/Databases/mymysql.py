import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="secret123",
    database="pubs"
)

print(f"Database object {mydb}")

# Query a table
# mycursor = mydb.cursor() # Use array positioning for each record.
mycursor = mydb.cursor(dictionary=True) # Use column names
mycursor.execute("SELECT * FROM authors")
result = mycursor.fetchall()

print("General query:")
for row in result:
    # print(row)
    print(f"{row["au_fname"]}\t{row["au_lname"]}\t{row["phone"]}")

print()
print()
print("WHERE query")

# Query with WHERE and parameters
sqlstatement="SELECT * FROM authors WHERE au_fname LIKE %s"
queryvalue=["A%"]
mycursor.execute(sqlstatement, queryvalue)
result = mycursor.fetchall()
for row in result:
    print(f"{row["au_fname"]}\t{row["au_lname"]}\t{row["phone"]}")

mydb.close()