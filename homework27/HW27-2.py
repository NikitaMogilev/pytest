from tabele import Table
from tabele import db

cursor = db.cursor()
table = Table()

table.salesman_table()
print('===== TASK 1 =====\n'
      'all info from table salesman ')
query = "SELECT *FROM salesman"
cursor.execute(query)
res = cursor.fetchall()
for row in res:
    print(row, '\n')

print('===== TASK 2 =====\n'
      'info from columns name and comission')
query = "SELECT name, comission FROM salesman"
cursor.execute(query)
res = cursor.fetchall()
for row in res:
    print(row, '\n')

print('===== TASK 3 =====\n'
      'salesman with comission more than 0.13')
query = "SELECT name FROM salesman WHERE comission>0.13"
cursor.execute(query)
res = cursor.fetchall()
for row in res:
    print(row, '\n')

print('===== TASK 4 =====\n'
      'salesman from Paris')
query = "SELECT name FROM salesman WHERE city='Paris'"
cursor.execute(query)
res = cursor.fetchall()
for row in res:
    print(row, '\n')

print('===== TASK 5 =====\n'
      'salesman with grade 200 ')
query = "SELECT *FROM salesman WHERE grade=200"
cursor.execute(query)
res = cursor.fetchall()
for row in res:
    print(row, '\n')

print('===== TASK 6 =====\n'
      'salesman with the biggest comission ')
query = "SELECT name, comission FROM test_db.salesman ORDER BY comission DESC"
cursor.execute(query)
res = cursor.fetchall()
name, comission = res[0]
print(name)

print('===== TASK 7 =====\n'
      'salesman with the smallest comission ')
query = "SELECT name, comission FROM test_db.salesman ORDER BY comission"
cursor.execute(query)
res = cursor.fetchall()
name, comission = res[0]
print(name)
db.close()
