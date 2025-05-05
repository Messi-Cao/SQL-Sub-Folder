import sqlite3

#database variable

Database = 'houses.db'

#define print_every_house to print all houses
def print_every_house():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their general details:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}") 
            print(f"Bedrooms: {house[3]}")
            print(f"Bathrooms: {house[4]}")
            print(f"Floors: {house[5]}")
            print(f"Basement: {house[6]}")
            print(f"Description: {house[7]}")
            print(f"Area Name: {house[11]}")
            print(f"Average Cost: ${house[9]}")

#define print_every_house_by_address to print all house addresses
def print_every_house_by_address():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their addresses:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}") 

#define print_every_house_by_rooms to print all house rooms
def print_every_house_by_rooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their room quantities:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}") 
            print(f"Bedrooms: {house[3]}")
            print(f"Bathrooms: {house[4]}")

#define print_every_house_by_address to print all house floors
def print_every_house_by_floors():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their floor quantities:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}")
            print(f"Floors: {house[5]}")

#define print_every_house_by_basement to print all house with basement availability
def print_every_house_by_basement():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their basement availability:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}")
            print(f"Basement: {house[6]}")

#define print_every_house_by_description to print all house descriptions
def print_every_house_by_description():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their descriptions:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}")
            print(f"Description: {house[7]}")

#define print_every_house_by_area to print all house area names
def print_every_house_by_area():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their area names:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}")
            print(f"Area Name: {house[11]}")

#define print_every_house_by_price to print all house price
def print_every_house_by_price():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of houses on auction in Pocket City with their average price:")
        for house in results:
            print(f"Address Number: {house[1]}") 
            print(f"Street: {house[2]}")
            print(f"Average Cost: ${house[9]}")

#Main code
while True:
    user_input = input(
"""
What would you like to do?
1. Print all houses
2. Print all houses by address only
3. Print all houses by address and rooms
4. Print all houses by address and floor
5. Print all houses by address and basement availabiliy
6. Print all houses by address and description
7. Print all houses by address and area
8. Print all houses by address and average cost
9. Quit
""")
    if user_input == "1":
        print_every_house()
    elif user_input == "2":
        print_every_house_by_address()
    elif user_input == "3":
        print_every_house_by_rooms()
    elif user_input == "4":
        print_every_house_by_floors()
    elif user_input == "5":
        print_every_house_by_basement()
    elif user_input == "6":
        print_every_house_by_description()
    elif user_input == "7":
        print_every_house_by_area()
    elif user_input == "8":
        print_every_house_by_price()
    elif user_input == "9":
        break
    else:
        print('Oops, this option is not available. Please try another one!')