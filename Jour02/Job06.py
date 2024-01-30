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

query = "SELECT SUM(capacite) AS capacite_totale FROM salle;"
cursor.execute(query)

result = cursor.fetchone()

capacite_totale = result[0]
print(f"La capacité de toutes les salles est de : {capacite_totale}")

cursor.close()
connection.close()
