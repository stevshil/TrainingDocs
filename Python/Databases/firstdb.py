import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "n3u3da!",
        database = "pubs2"
    )
    print(mydb)
except Exception as e:
    print(f"Error connecting to database {e}")

try: 
    sakila = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "n3u3da!",
        database = "sakila"
    )
    print(sakila)
except Exception as e:
    print(f"Error connecting to database {e}")
    
mystarter = input("Enter first character of firstname: ")

sakcursor = sakila.cursor(dictionary=True)
# sakcursor.execute("SELECT * FROM actor")
# sakcursor.execute("SELECT * FROM actor WHERE first_name LIKE 'A%'")
# sakcursor.execute(f"SELECT * FROM actor WHERE first_name LIKE '{mystarter}%'") # BAD!!!
sqlstmt = "SELECT * FROM actor WHERE first_name LIKE %s"
sqlarg = [mystarter+"%"]
try:
    sakcursor.execute(sqlstmt,sqlarg)
    authors = sakcursor.fetchall()

    for author in authors:
        # print( author[1] + " " + author[2] )
        # print(author)
        print( author["first_name"] + " " + author["last_name"])
except Exception as e:
    print(f"Error in SQL statement: {e}")
    
try:
    sakcursor.execute('''INSERT INTO ACTOR (first_name,last_name)
                  VALUES('steve','shilling')''')
    sakila.commit()
    print("Inserted into database")
except Exception as e:
    print(f"Error in insert: {e}")

sakcursor.close()

try:
    mydb.close()
except:
    pass

try:
    sakila.close()
except:
    pass