import sqlite3

conn=sqlite3.connect('bd_2')

cursor=conn.cursor()

#добавляем значения в таблицу Clients
cursor.execute('insert into Clients (Name,Address) Values (?,?)', ("Bob", "Moscow"))
cursor.execute('insert into Clients (Name,Address) Values (?,?)', ("Mike", "Peterburg"))
cursor.execute('insert into Clients (Name,Address) Values (?,?)', ("Tom", "Penza"))

#добавляем значения в таблицу Products
cursor.execute('insert into Products (Name,Price,Count) Values (?,?,?)', ("Milk",100,10))
cursor.execute('insert into Products (Name,Price,Count) Values (?,?,?)', ("Vino",500,2))
cursor.execute('insert into Products (Name,Price,Count) Values (?,?,?)', ("Bread",15,50))

query = 'SELECT Name from Products'
cursor.execute(query)
print(cursor.fetchall())

query = 'SELECT Name from Clients'
cursor.execute(query)
print(cursor.fetchall())





