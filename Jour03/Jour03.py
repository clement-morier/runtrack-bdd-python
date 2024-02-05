import mysql.connector
from tkinter import Tk, Label, Button, Entry, Listbox, Scrollbar, messagebox

# Connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DouDou13380!",
    database="store"
)
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        description TEXT,
        price INT,
        quantity INT,
        id_category INT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS category (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
""")

cursor.execute("INSERT INTO category (name) VALUES ('Electronics')")
cursor.execute("INSERT INTO category (name) VALUES ('Clothing')")
db.commit()

def update_product_list():
    product_listbox.delete(0, 'end')
    cursor.execute("SELECT id, name, quantity, price FROM product")
    products = cursor.fetchall()
    for product in products:
        product_listbox.insert('end', f"{product[0]} - {product[1]} - Quantity: {product[2]} - Price: {product[3]}")

def add_product():
    name = entry_name.get()
    description = entry_description.get()
    price = int(entry_price.get())
    quantity = int(entry_quantity.get())
    category_id = int(entry_category_id.get())

    cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)",
                   (name, description, price, quantity, category_id))
    db.commit()
    update_product_list()

def delete_product():
    selected_index = product_listbox.curselection()
    if selected_index:
        selected_id = int(product_listbox.get(selected_index)[0])
        cursor.execute("DELETE FROM product WHERE id = %s", (selected_id,))
        db.commit()
        update_product_list()

root = Tk()
root.title("Gestion de Stock")

label_name = Label(root, text="Nom du produit:")
label_name.grid(row=0, column=0)

entry_name = Entry(root)
entry_name.grid(row=0, column=1)

label_description = Label(root, text="Description:")
label_description.grid(row=1, column=0)

entry_description = Entry(root)
entry_description.grid(row=1, column=1)

label_price = Label(root, text="Prix:")
label_price.grid(row=2, column=0)

entry_price = Entry(root)
entry_price.grid(row=2, column=1)

label_quantity = Label(root, text="Quantité:")
label_quantity.grid(row=3, column=0)

entry_quantity = Entry(root)
entry_quantity.grid(row=3, column=1)

label_category_id = Label(root, text="ID Catégorie:")
label_category_id.grid(row=4, column=0)

entry_category_id = Entry(root)
entry_category_id.grid(row=4, column=1)

button_add = Button(root, text="Ajouter Produit", command=add_product)
button_add.grid(row=5, column=0, columnspan=2)

button_delete = Button(root, text="Supprimer Produit", command=delete_product)
button_delete.grid(row=6, column=0, columnspan=2)

product_listbox = Listbox(root, selectmode="single")
product_listbox.grid(row=0, column=2, rowspan=7)

scrollbar = Scrollbar(root, orient="vertical", command=product_listbox.yview)
scrollbar.grid(row=0, column=3, rowspan=7, sticky="ns")

product_listbox.config(yscrollcommand=scrollbar.set)

update_product_list()

root.mainloop()