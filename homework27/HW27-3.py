from tabele import Table
from tabele import db

cursor = db.cursor()
table = Table()

table.computer_table()

print('===== TASK 1 =====\n'
      'Summary costs of components ')
query = "SELECT SUM(PRO_PRICE) FROM test_db.PC"
cursor.execute(query)
res = cursor.fetchall()[0][0]
print(res)

print('===== TASK 2=====\n'
      'average cost  of components ')
query = "SELECT AVG(PRO_PRICE) FROM test_db.PC"
cursor.execute(query)
res = cursor.fetchall()[0][0]
print(round(res, 2))

print('===== TASK 3=====\n'
      'components with price between 200 and 600 \n'
      'uniq ID| PRO_ID | PRO_NAME | PRO_PRICE | PRO_COM')
query = "SELECT * FROM PC WHERE PRO_PRICE BETWEEN 200 AND 600"
cursor.execute(query)
res = cursor.fetchall()
for row in res:
    print(row, '\n')

print('===== TASK 4 =====\n'
      'component with the biggest price ')
query = "SELECT PRO_NAME, PRO_PRICE FROM PC ORDER BY PRO_PRICE DESC"
cursor.execute(query)
res = cursor.fetchall()
pro_name, pro_price = res[0]
print(pro_name)

print('===== TASK 5 =====\n'
      'component with the biggest price ')
query = "SELECT PRO_NAME, PRO_PRICE FROM PC ORDER BY PRO_PRICE"
cursor.execute(query)
res = cursor.fetchall()
pro_name, pro_price = res[0]
print(pro_name)

db.close()
