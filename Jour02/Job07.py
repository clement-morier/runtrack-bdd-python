import mysql.connector

class Salarie:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def get_all_employees(self):
        query = """
            SELECT employe.nom AS nom_employe, employe.prenom, employe.salaire, service.nom AS nom_service
            FROM employe
            JOIN service ON employe.id_service = service.id;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

host = "localhost"
user = "root"
password = "DouDou13380!"
database = "Entreprise"

salarie_manager = Salarie(host, user, password, database)
employees_with_service = salarie_manager.get_all_employees()

for employee in employees_with_service:
    print(employee)

salarie_manager.close_connection()
