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
        print("The following are the list of houses on auction in Pocket City with its general details:")
        for house in results:
            print(f"Address number: {house[1]}") 
            print(f"Street: {house[2]}") 
            print(f"Bedrooms: {house[3]}")
            print(f"Bathrooms: {house[4]}")
            print(f"Floors: {house[5]}")
            print(f"Basement: {house[6]}")
            print(f"Description: {house[7]}")
            print(f"Area: {house[8]}")
            print(f"Average Cost: ${house[9]}")
#Main code
while True:
    user_input = input(
"""
What would you like to do?
1. Print all houses
2. Quit
""")
    if user_input == "1":
        print_every_house()
    elif user_input == "2":
        break
    else:
        print('Oops, this option is not available. Please try another one!')