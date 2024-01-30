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

query = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
cursor.execute(query)
result = cursor.fetchone()

superficie_totale = result[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

cursor.close()
connection.close()
