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

#define print_every_house_with_two_bedrooms
def print_every_house_with_two_bedrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bedrooms = 2;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of two bedroom houses on auction in Pocket City:")
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

#define print_every_house_with_three_bedrooms
def print_every_house_with_three_bedrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bedrooms = 3;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of three bedroom houses on auction in Pocket City:")
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

#define print_every_house_with_four_bedrooms
def print_every_house_with_four_bedrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bedrooms = 4;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of four bedroom houses on auction in Pocket City:")
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

#define print_every_house_with_five_bedrooms
def print_every_house_with_five_bedrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bedrooms = 5;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of five bedroom houses on auction in Pocket City:")
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

#define print_every_house_with_six_bedrooms
def print_every_house_with_six_bedrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bedrooms = 6;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of six bedroom houses on auction in Pocket City:")
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

#define print_every_house_with_seven_bedrooms
def print_every_house_with_seven_bedrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bedrooms = 7;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of seven bedroom houses on auction in Pocket City:")
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

#define print_every_house_with_one_bathroom
def print_every_house_with_one_bathroom():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 1;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of one bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_two_bathrooms
def print_every_house_with_two_bathrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 2;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of two bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_two_point_five_bathrooms
def print_every_house_with_two_point_five_bathrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 2.5;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of 2.5 bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_three_bathrooms
def print_every_house_with_three_bathrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 3;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of three bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_four_point_five_bathrooms
def print_every_house_with_four_point_five_bathrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 4.5;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of 4.5 bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_five_bathrooms
def print_every_house_with_five_bathrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 5;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of five bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_ten_bathrooms
def print_every_house_with_ten_bathrooms():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE bathrooms = 10;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of ten bathroom houses on auction in Pocket City:")
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

#define print_every_house_with_one_floor
def print_every_house_with_one_floor():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE floor_no = 1;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of single storey houses on auction in Pocket City:")
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

#define print_every_house_with_two_floors
def print_every_house_with_two_floors():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE floor_no = 2;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of two storey houses on auction in Pocket City:")
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

#define print_every_house_with_three_floors
def print_every_house_with_three_floors():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE floor_no = 3;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of three storey houses on auction in Pocket City:")
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

#define print_every_house_with_four_floors
def print_every_house_with_four_floors():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM house JOIN area ON house.area_id = area.id WHERE floor_no = 4;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of four storey houses on auction in Pocket City:")
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

#define print_every_house_with_basement
def print_every_house_with_basement():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM house JOIN area ON house.area_id = area.id WHERE basement = "Yes";'
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of four storey houses on auction in Pocket City:")
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

#define print_every_house_without_basement
def print_every_house_without_basement():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM house JOIN area ON house.area_id = area.id WHERE basement = "No";'
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from house
        #print them nicely
        print("The following are the list of four storey houses on auction in Pocket City:")
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

#Main code of the application
while True:
    user_input = input(
"""
Welcome user, to the application of 'Pocket City House Selector'!
In this application, you can explore a range of houses on auction in Pocket City.
Press '0' whenever you need to leave a selection page. 
Please keep in mind you must type the exact same character shown to the left of the option. 
(E.g. When it displays "[1]. Print all houses", you must type exactly that character (in this case it's 1) into the input to avoid errors.)
What would you like to do?
1. Print all houses
2. Print all houses by address only
3. Print all houses by address and rooms
4. Print all houses by address and floor
5. Print all houses by address and basement availabiliy
6. Print all houses by address and description
7. Print all houses by address and area
8. Print all houses by address and average cost
9. Choose from custom list (WIP)
0. Quit
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
        #Custom selection
        while True:
            try: 
                custom_input = input(
"""
Please choose from the following:
1. Bedrooms
2. Bathrooms
3. Floors
4. Basement Availability
0. Quit
""")
                #bedroom quantity
                if custom_input == "1":
                    while True:
                        bedroom_quantity = input("Choose your bedroom quantity (To exit, please press '0'): ")
                        if bedroom_quantity == "2":
                            print_every_house_with_two_bedrooms()
                        elif bedroom_quantity == "3":
                            print_every_house_with_three_bedrooms()
                        elif bedroom_quantity == "4":
                            print_every_house_with_four_bedrooms()
                        elif bedroom_quantity == "5":
                            print_every_house_with_five_bedrooms()
                        elif bedroom_quantity == "6":
                            print_every_house_with_six_bedrooms()
                        elif bedroom_quantity == "7":
                            print_every_house_with_seven_bedrooms()
                        elif bedroom_quantity == "0":
                            break
                        else:
                            print('Sorry, we currently do not have this option. Please come back after!')
                #bathroom quantity
                elif custom_input == "2":
                    while True:
                        bathroom_quantity = input("Choose your bathroom quantity (To exit, please press '0'): ")
                        if bathroom_quantity == "1":
                            print_every_house_with_one_bathroom()
                        elif bathroom_quantity == "2":
                            print_every_house_with_two_bathrooms()
                        elif bathroom_quantity == "2.5":
                            print_every_house_with_two_point_five_bathrooms()
                        elif bathroom_quantity == "3":
                            print_every_house_with_three_bathrooms()
                        elif bathroom_quantity == "4.5":
                            print_every_house_with_four_point_five_bathrooms()
                        elif bathroom_quantity == "5":
                            print_every_house_with_five_bathrooms()
                        elif bathroom_quantity == "10":
                            print_every_house_with_ten_bathrooms()
                        elif bathroom_quantity == "0":
                            break
                        else:
                            print('Sorry, we currently do not have this option. Please come back after!')
                #floor quantity
                elif custom_input == "3":
                    while True: 
                        floor_quantity = input("Choose your floor quantity (To exit, please press '0'): ")
                        if floor_quantity == "1":
                            print_every_house_with_one_floor()
                        elif floor_quantity == "2":
                            print_every_house_with_two_floors()
                        elif floor_quantity == "3":
                            print_every_house_with_three_floors()
                        elif floor_quantity == "4":
                            print_every_house_with_four_floors()
                        elif floor_quantity == "0":
                            break
                        else:
                            print('Sorry, we currently do not have this option. Please come back after!')
                #basement availability
                elif custom_input == "4":
                    basement_availability = input(
"""
Choose 'yes' or 'no' for your basement availability.
To exit, please press '0': 
""").lower()
                    if basement_availability == "yes":
                        print_every_house_with_basement()
                    elif basement_availability == "no":
                        print_every_house_without_basement()
                    elif basement_availability == "0":
                        break
                    else:
                        print("You may only choose 'yes' or 'no' for this option, please try again.")
                #To get out of the selection
                elif custom_input == "0":
                    break
                #Invalid input message
                else:
                    print('Oops, invalid input! Please try again!')
            #Another invalid input message
            except ValueError: 
                print('Oops, invalid input! Please try again!')
    #break out of code
    elif user_input == "0":
        break
    #unavailable option message
    else:
        print('Oops, this option is not available. Please try another one!')