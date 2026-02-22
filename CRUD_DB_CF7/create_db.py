import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        ) 

        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"Error: {e} occured")

    return connection

def create_database(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print("Database created succesfully")
    except Error as e:
        print(f"Error: {e} occured")
    finally:
        cursor.close()

def main():
    connect = create_connection('localhost', 'root', 'my_pass')

    if connect:
        create_db_query = "CREATE DATABASE coding2025"
        create_database(connect, create_db_query)
        connect.close()
        print("MySQL connection is closed.")

if __name__ == "__main__":
    main()  