import mysql.connector

def insert_data(id, name, country):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="roottoor",
        database="29_ece"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO city(id, name, country) VALUES (%s, %s, %s)"
    val = (id, name, country)
    mycursor.execute("select * from city")
     
    result=mycursor.fetchall()
    for row in result:
        print(row)

    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

    mycursor.close()
    mydb.close()

id = input("Enter the ID: ")
name = input("Enter the name: ")
country = input("Enter the country: ")
insert_data(id, name, country)
