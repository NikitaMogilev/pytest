import mysql.connector as mysql
from data_base import data_base_create

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Nikita1988!",
    database=data_base_create()
)


class Table:
    def __init__(self):
        self.cursor2 = None
        self.cursor1 = None
        self.cursor = None

    def orders_table(self):
        self.cursor = db.cursor()
        try:
            self.cursor.execute("CREATE TABLE orders (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                "ord_no INT, "
                                "purch_amt FLOAT, "
                                "ord_date DATE, "
                                "customer_id INT, "
                                "salesman_id INT)")
            self.cursor.execute("ALTER TABLE orders ADD UNIQUE(ord_no)")

            values = [
                (70001, 150.5, '2012-10-05', 3005, 5002),
                (70009, 270.65, '2012-09-10', 3001, 5005),
                (70002, 65.26, '2012-10-05', 3002, 5001),
                (70004, 110.5, '2012-08-17', 3009, 5003),
                (70007, 948.5, '2012-09-10', 3005, 5002),
                (70005, 2400.6, '2012-07-27', 3007, 5001),
                (70008, 5760, '2012-09-10', 3002, 5001),
                (70010, 1983.43, '2012-10-10', 3004, 5006),
                (70003, 2480.4, '2012-10-10', 3009, 5003),
                (70012, 250.45, '2012-06-27', 3008, 5002),
                (70011, 75.29, '2012-08-17', 3003, 5007),
                (70013, 3045.6, '2012-04-25', 3002, 5001)
            ]
            query = "INSERT IGNORE INTO orders " \
                    "(ord_no, " \
                    "purch_amt, " \
                    "ord_date, " \
                    "customer_id, " \
                    "salesman_id) " \
                    "VALUES (%s, %s, %s, %s, %s) "
            self.cursor.executemany(query, values)
            db.commit()
        except:
            values = [
                (70001, 150.5, '2012-10-05', 3005, 5002),
                (70009, 270.65, '2012-09-10', 3001, 5005),
                (70002, 65.26, '2012-10-05', 3002, 5001),
                (70004, 110.5, '2012-08-17', 3009, 5003),
                (70007, 948.5, '2012-09-10', 3005, 5002),
                (70005, 2400.6, '2012-07-27', 3007, 5001),
                (70008, 5760, '2012-09-10', 3002, 5001),
                (70010, 1983.43, '2012-10-10', 3004, 5006),
                (70003, 2480.4, '2012-10-10', 3009, 5003),
                (70012, 250.45, '2012-06-27', 3008, 5002),
                (70011, 75.29, '2012-08-17', 3003, 5007),
                (70013, 3045.6, '2012-04-25', 3002, 5001)
            ]
            query = "INSERT IGNORE INTO orders " \
                    "(ord_no, " \
                    "purch_amt, " \
                    "ord_date, " \
                    "customer_id, " \
                    "salesman_id) " \
                    "VALUES (%s, %s, %s, %s, %s) "
            self.cursor.executemany(query, values)
            db.commit()
            print(self.cursor.rowcount, "records inserted")

    def salesman_table(self):
        self.cursor = db.cursor()
        try:
            self.cursor.execute("CREATE TABLE salesman (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                 "salesman_id INT, "
                                 "name VARCHAR(255), "
                                 "city VARCHAR(255), "
                                 "comission FLOAT, "
                                 "grade INT)")

            self.cursor.execute("ALTER TABLE salesman ADD UNIQUE(salesman_id)")

            values = [
                (5001, 'James_Hoog', 'New York', 0.15, 100),
                (5002, 'Nail_Knite', 'Paris', 0.13, 200),
                (5003, 'Pit_Alex', 'London', 0.11, 150),
                (5004, 'Mc_Lyon', 'Paris', 0.14, 50),
                (5005, 'Paul_Adam', 'Rome', 0.13, 200),
                (5006, 'Lauson_Hen', 'San Jose', 0.12, 300),
            ]

            query = "INSERT IGNORE INTO salesman " \
                    "(salesman_id, " \
                    "name, " \
                    "city, " \
                    "comission, " \
                    "grade) " \
                    "VALUES (%s, %s, %s, %s, %s)"
            self.cursor.executemany(query, values)
            db.commit()
            print(self.cursor.rowcount, "records inserted")
        except:
            values = [
                (5001, 'James_Hoog', 'New York', 0.15, 100),
                (5002, 'Nail_Knite', 'Paris', 0.13, 200),
                (5003, 'Pit_Alex', 'London', 0.11, 150),
                (5004, 'Mc_Lyon', 'Paris', 0.14, 50),
                (5005, 'Paul_Adam', 'Rome', 0.13, 200),
                (5006, 'Lauson_Hen', 'San Jose', 0.12, 300),
            ]
            query = "INSERT IGNORE INTO salesman " \
                    "(salesman_id, " \
                    "name, " \
                    "city, " \
                    "comission, " \
                    "grade) " \
                    "VALUES (%s, %s, %s, %s, %s)"
            self.cursor.executemany(query, values)
            db.commit()
            print(self.cursor.rowcount, "records inserted")

    def computer_table(self):
        self.cursor = db.cursor()
        try:
            self.cursor.execute("CREATE TABLE PC (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                                "PRO_ID INT, "
                                "PRO_NAME VARCHAR(255), "
                                "PRO_PRICE INT, "
                                "PRO_COM FLOAT)")

            self.cursor.execute("ALTER TABLE PC ADD UNIQUE(PRO_ID)")

            values = [(101, 'Mother Board', 3200, 15),
                      (102, 'Key Board', 450, 16),
                      (103, 'ZIP drive', 250, 14),
                      (104, 'Speaker', 550, 16),
                      (105, 'Monitor', 5000, 11),
                      (106, 'DVD drive', 900, 12),
                      (107, 'CD drive', 800, 2),
                      (108, 'Printer', 2600, 13),
                      (109, 'Refill cartridge', 350, 13),
                      (110, 'Mouse', 250, 12)]

            query = "INSERT IGNORE INTO PC " \
                    "(PRO_ID, " \
                    "PRO_NAME," \
                    "PRO_PRICE, " \
                    "PRO_COM)" \
                    "VALUES (%s, %s, %s, %s) "
            self.cursor.executemany(query, values)
            db.commit()
            print(self.cursor.rowcount, "records inserted")
        except:

            values = [(101, 'Mother Board', 3200, 15),
                      (102, 'Key Board', 450, 16),
                      (103, 'ZIP drive', 250, 14),
                      (104, 'Speaker', 550, 16),
                      (105, 'Monitor', 5000, 11),
                      (106, 'DVD drive', 900, 12),
                      (107, 'CD drive', 800, 2),
                      (108, 'Printer', 2600, 13),
                      (109, 'Refill cartridge', 350, 13),
                      (110, 'Mouse', 250, 12)]

            query = "INSERT IGNORE INTO PC " \
                    "(PRO_ID, " \
                    "PRO_NAME," \
                    "PRO_PRICE, " \
                    "PRO_COM)" \
                    "VALUES (%s, %s, %s, %s) "
            self.cursor.executemany(query, values)
            db.commit()
            print(self.cursor.rowcount, "records inserted")
