import mysql.connector

host = "localhost"
user = "root"
password = "DouDou13380!"
database = "LaPlateforme"

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = connection.cursor()

query = "SELECT nom, capacite FROM salle;"
cursor.execute(query)

result = cursor.fetchall()
L=[]
for row in result:
    L.append(f"({row[0]},{row[1]})")
print(L)
cursor.close()
connection.close()
