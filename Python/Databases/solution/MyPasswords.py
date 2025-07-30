import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="secret123"
    )
except Exception as e:
    print(f"Failed to connect to the database {e}")
    exit(1)

# Create the database MyPasswords
try:
    mycursor = mydb.cursor(dictionary=True, buffered=True)
    mycursor.execute("CREATE DATABASE IF NOT EXISTS MyPasswords")
    mycursor.execute("USE MyPasswords")
except Exception as e:
    print(f"Failed to create the database {e}")

# Create the tables
try:
    mycursor.execute("""CREATE TABLE IF NOT EXISTS Passwords(
                     Name VARCHAR(50) PRIMARY KEY,
                     LoginID VARCHAR(150) NOT NULL,
                     Password VARCHAR(32) NOT NULL,
                     URL VARCHAR(150),
                     Notes TEXT,
                     DeleteDate DATETIME,
                     CreationDate DATETIME default CURRENT_TIMESTAMP,
                     ModificationDate DATETIME
                     )""")
except Exception as e:
    print(f"Failed to create Passwords table {e}")
    exit(2)

try:
    mycursor.execute("""CREATE TABLE IF NOT EXISTS Certificates(
                     Name VARCHAR(50) PRIMARY KEY,
                     ServerName VARCHAR(50) NOT NULL,
                     Certificate VARCHAR(250) NOT NULL,
                     Notes TEXT,
                     DeleteDate DATETIME,
                     CreationDate DATETIME default CURRENT_TIMESTAMP,
                     ModificationDate DATETIME
                     )""")
except Exception as e:
    print(f"Failed to create Certificates table {e}")
    exit(3)

mydb.commit()

sql = "INSERT INTO Passwords (Name, LoginID, Password, URL) VALUES(%s,%s,%s,%s)"
data = [('Steve','superuser','secret123','http://there.com'),
                     ('Jack','slipperysnake','letmein231','http://python.com'),
                     ('Fridah','lovescoffee','letitmarinade','http://java.com')]

sql2 = "INSERT INTO Passwords(Name,LoginID,Password,URL,DeleteDate) VALUES(%s,%s,%s,%s,%s)"
data2 = ('Nick','omnipresent','nopasswordrequired','http://thatsmeinthecorner.com','1970-01-01 12:00:00')

try:
    for row in data:
        mycursor.execute(sql,row)
    mycursor.execute(sql2,data2)
    mydb.commit()
except Exception as e:
    print(f"Failed to insert data {e}")
    exit(4)

mydb.close()