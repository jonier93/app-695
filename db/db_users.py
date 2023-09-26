import pymysql
from pymysql import MySQLError, connect

user = "admin"
password = "12345678"
db_name = "db_695"
ip = "db-instance.comtpesdvdbc.us-east-2.rds.amazonaws.com" 
table =  "users"
connection = ""

def connectionSQL():
    try:
        global connection
        connection = connect(host=ip,
                             user=user,
                             password=password,
                             db=db_name)
        print("Succesful connection")
    except MySQLError as ex:
        print(ex)

def insert_record(name, lastName, id, age):
    try:
        instruction = "INSERT INTO " + table + " VALUES ('"+name+"', '"+lastName+"', "+id+", "+age+")"
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("User registered")
        
    except MySQLError as ex:
        print(ex)
    
def consult_user(id):
    try:
        instruction = "SELECT * FROM " + table + " WHERE id=" + id + ";" 
        cursor = connection.cursor()
        cursor.execute(instruction)
        result = cursor.fetchall()
        return result
    except MySQLError as ex:
        print(ex)