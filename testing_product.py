import sqlite3

#database variable

Database = 'product.db'

#define print_every_car to print all car models
def print_every_product():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM product"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of products issued recently:")
        for product in results:
            print(f"Name: {product[1]}") 
            print(f"Issued Date: {product[2]}") 

def print_every_manufacturer():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM manufacturer;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of manufacturers of recently issued products:")
        for manufacturer in results:
            print(f"Name: {manufacturer[1]}") 

#Main code
while True:
    user_input = input(
"""
What would you like to do?
1. Print all products with their issued date
2. Print all manufacturers
3. Quit
""")
    if user_input == "1":
        print_every_product()
    elif user_input == "2":
        print_every_manufacturer()
    elif user_input == "3":
        break
    else:
        print("Invalid option")