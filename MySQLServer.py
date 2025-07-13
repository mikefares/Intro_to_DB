import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "username",
        password = "password"
    )

    myCursor = mydb.cursor()

    myCursor.execute("DROP DATABASE alx_book_Store")

    myCursor.execute("CREATE DATABASE alx_book_store")

    print("Databasae 'alx_book_Store' created successfully!")

except:
    print("Cannot connect to database. Enter correct credentials")

finally:
    myCursor.close()
    mydb.close()