# Install mysql connector:
#   pip install mysql-connector-python
import mysql.connector

cnx = mysql.connector.connect(user='root', password='p4ssword',
                              host='127.0.0.1',
                              database='oct7')

cursor = cnx.cursor()

# test on Persons table
add_person = "INSERT INTO PersonS (lastname, FirstName, Age) VALUES ('Gretsky', 'Wayne', 60); "
cursor.execute(add_person)

# Creating and using a new database
cursor.execute("DROP DATABASE IF EXISTS test_creation;")
cursor.execute("CREATE DATABASE test_creation;")
cursor.execute("USE test_creation")

#Inserting data into persons table


# Create tables
add_table_sport = "CREATE TABLE sports (SportID int, Sport varchar(255));"
cursor.execute(add_table_sport)

insert_sports = "INSERT INTO sports VALUES (1, 'Basketball'), (2, 'Football'), (3, 'Hockey');"
cursor.execute(insert_sports)

# Query values
# cursor.execute("SELECT lastname, persons.sport, sportid FROM persons JOIN sports ON persons.sport=sports.sport;")

while True:
    check = input("Do you want to add a player to the database? (y,n)")
    if check != "y":
        break
    
    personID = int(input("Enter player ID: "))
    firstname = input("Enter player first name: ")
    lastname = input("Enter player last name: ")
    age = input("Enter Age: ")
    # INSERT INTO persons VALUES (11, 'firstname', 'lastname', 'city', 'sport');
    query = "INSERT INTO persons VALUES (" + str(personID) + ", '"+ firstname +"', '" + lastname + "', '" + age + "');"
    cursor.execute("USE oct7")
    cursor.execute(query)


cursor.execute("USE oct7")
cursor.execute("SELECT * FROM persons;")
for row in cursor:
     print(row)

cnx.commit()

cursor.close()
cnx.close()