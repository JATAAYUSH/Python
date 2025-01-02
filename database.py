import mysql.connector
if __name__=='__main__':
    connection=mysql.connector.connect(
        user="root",
        password="@aayush3095",
        host="localhost",
        database="user_data12"
    )
    print(connection.is_connected())
    cursor=connection.cursor()
    query1="CREATE TABLE Student(Name VARCHAR(50),Enrollment_NO int,Division VARCHAR(50),Institude VARCHAR(50));"
    query2="INSERT INTO Student(Name,Enrollment_NO,Division,Institude) VALUES ('Aayush Jat',0003,'4b4','PIT'),('Anurag Jat',0083,'4b5','PIT'),('Rohan Panwar',0038,'4b4','PIT'),('Rahul Singh',063,'4b5','PIT');"
    query3="UPDATE Student SET Name='Gautam Maru' WHERE Name='Anurag Jat'"
    query4="ALTER TABLE Student RENAME COLUMN Institude TO Institute;"
    query5="DELETE FROM Student WHERE Name='Rahul Singh';"
    query6="CREATE VIEW 4B4_Students AS SELECT Name, Enrollment_NO FROM Student WHERE Division='4b4';"
    query7="DROP TABLE Student"
    query8="DROP VIEW 4B4_StudentS;"
    # cursor.execute(query1)
    # cursor.execute(query2)
    # cursor.execute(query3)
    # cursor.execute(query4)
    # cursor.execute(query5)
    # cursor.execute(query6)
    cursor.execute(query7)
    cursor.execute(query8)
    connection.commit()
    # cursor.execute("SELECT* FROM student")
    # cursor.execute("SELECT* FROM 4b4_students")
    
    # results=cursor.fetchall()
    # column_names = [i[0] for i in cursor.description] 
    # print(column_names)
    # for row in results:
    #     print(row)

# write a program to perfom the query of update,create,
# delete and view throught the python and show data: 