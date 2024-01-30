import mysql.connector

class ZooManager:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def create_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = """
            INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine)
            VALUES (%s, %s, %s, %s, %s);
        """
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.connection.commit()

    def create_cage(self, superficie, capacite_max):
        query = """
            INSERT INTO cage (superficie, capacite_max)
            VALUES (%s, %s);
        """
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s;"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_cage(self, cage_id):
        query = "DELETE FROM cage WHERE id = %s;"
        values = (cage_id,)
        self.cursor.execute(query, values)
        self.connection.commit()

    def modify_animal(self, animal_id, new_nom, new_race, new_id_cage, new_date_naissance, new_pays_origine):
        query = """
            UPDATE animal
            SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s
            WHERE id = %s;
        """
        values = (new_nom, new_race, new_id_cage, new_date_naissance, new_pays_origine, animal_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def modify_cage(self, cage_id, new_superficie, new_capacite_max):
        query = """
            UPDATE cage
            SET superficie = %s, capacite_max = %s
            WHERE id = %s;
        """
        values = (new_superficie, new_capacite_max, cage_id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_all_animals(self):
        query = "SELECT * FROM animal;"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_animals_in_cages(self):
        query = """
            SELECT animal.nom AS nom_animal, animal.race, cage.id AS id_cage, cage.superficie, cage.capacite_max
            FROM animal
            JOIN cage ON animal.id_cage = cage.id;
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def calculate_total_cage_area(self):
        query = "SELECT SUM(superficie) AS total_area FROM cage;"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

host = "localhost"
user = "root"
password = "DouDou13380!"
database = "zoo"

zoo_manager = ZooManager(host, user, password, database)

zoo_manager.create_animal("Lion", "Africain", 1, "2022-01-01", "Afrique")

zoo_manager.create_cage(100.00, 10)

zoo_manager.modify_animal(1, "Lion", "Africain", 1, "2022-01-01", "Afrique")

zoo_manager.modify_cage(1, 120.00, 15)

zoo_manager.delete_animal(1)

zoo_manager.delete_cage(1)

print("Liste des animaux dans le zoo:")
animals = zoo_manager.get_all_animals()
for animal in animals:
    print(animal)

print("\nListe des animaux dans les cages:")
animals_in_cages = zoo_manager.get_animals_in_cages()
for animal_in_cage in animals_in_cages:
    print(animal_in_cage)

total_cage_area = zoo_manager.calculate_total_cage_area()
print(f"\nSuperficie totale des cages : {total_cage_area} m2")

zoo_manager.close_connection()
