import mysql.connector as mysql


def data_base_create():
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="Nikita1988!",
    )

    cursor = db.cursor()
    data_base_name = "test_db"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {data_base_name}")
    print(cursor.fetchall())
    return data_base_name
