
from tabele import Table
from tabele import db

cursor = db.cursor()
table = Table()
table.orders_table()


print('===== TASK 1 =====')
query = "SELECT ord_no, ord_date, purch_amt FROM orders WHERE salesman_id=5002"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 2 =====')
query = "SELECT DISTINCT salesman_id FROM orders"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 3 =====')
query = "SELECT ord_date, salesman_id, ord_no, purch_amt FROM orders"
cursor.execute(query)
print(cursor.fetchall())

print('===== TASK 4 =====')
query = "SELECT * FROM orders WHERE ord_no BETWEEN 70001 AND 70007"
cursor.execute(query)
print(cursor.fetchall())

db.close()

table.salesman_table()