import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name, port):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name,
            port = port
        ) 

        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: {e} occured")

    return connection

def insert_teacher(connection, teacher):
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO teachers (id, firstname, lastname, age) VALUES (%s, %s, %s, %s)",
            teacher
        )
        connection.commit()
        print("Teacher inserted!")
    except Error as e:
        print(f"Error {e} occured")
        connection.rollback()
    finally:
        cursor.close()

def main():
    connect = create_connection('localhost', 'root', 'my_pass', 'coding2025', '3306')

    if connect:
        teacher = (1, "Bob", "M.", 45)
        insert_teacher(connect, teacher)
        connect.close()
        print("MySQL connection is closed.")

if __name__ == "__main__":
    main()          