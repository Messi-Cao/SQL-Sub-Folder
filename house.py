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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print(f"Bedrooms: {house[3]}")
           print(f"Bathrooms: {house[4]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print(f"Floors: {house[5]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print(f"Basement: {house[6]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print(f"Description: {house[7]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print(f"Area Name: {house[11]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
       for house in results:
           print(f"Address Number: {house[1]}")
           print(f"Street: {house[2]}")
           print(f"Average Cost: ${house[9]}")
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


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
       print("----------------------------------------")
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
           print("----------------------------------------")


#Main code
#quit variable
quit = 0
#variables for main menu
print_all = 1
print_all_by_address = 2
print_all_by_address_and_rooms = 3
print_all_by_address_and_floor = 4
print_all_by_address_and_basement = 5
print_all_by_address_and_description = 6
print_all_by_address_and_area_name = 7
print_all_by_address_and_cost = 8
print_custom = 9
#custom selection page variables
bedrooms = 1
bathrooms = 2
floors = 3
basement = 4
#variables for bedroom quantity
two_bedrooms = 2
three_bedrooms = 3
four_bedrooms = 4
five_bedrooms = 5
six_bedrooms = 6
seven_bedrooms = 7
#variables for bathroom quantity
one_bathroom = 1
two_bathrooms = 2
two_point_five_bathrooms = 2.5
three_bathrooms = 3
four_point_five_bathrooms = 4.5
five_bathrooms = 5
ten_bathrooms = 10
#variables for floor quantity
one_floor = 1
two_floors = 2
three_floors = 3
four_floors = 4
#variables for basement availability
yes = "yes"
no = "no"
#Main functioning code of the application
while True:
   user_input = int(input(
"""
Welcome user, to the application of 'Pocket City House Selector' where you can explore 12 Pocket City houses on auction!
Press '0' whenever you need to leave a selection page.
Please keep in mind you must type the exact same character shown to the left of the option.
(E.g. When it displays "1. Print all houses", you must type exactly that character ("1") into the input to avoid errors.)
What would you like to do?
1. Print all houses
2. Print all houses by address only
3. Print all houses by address and rooms
4. Print all houses by address and floor
5. Print all houses by address and basement availability
6. Print all houses by address and description
7. Print all houses by address and area name
8. Print all houses by address and average cost
9. Choose from custom list
0. Quit application
"""))
   if user_input == print_all:
       print_every_house()
   elif user_input == print_all_by_address:
       print_every_house_by_address()
   elif user_input == print_all_by_address_and_rooms:
       print_every_house_by_rooms()
   elif user_input == print_all_by_address_and_floor:
       print_every_house_by_floors()
   elif user_input == print_all_by_address_and_basement:
       print_every_house_by_basement()
   elif user_input == print_all_by_address_and_description:
       print_every_house_by_description()
   elif user_input == print_all_by_address_and_area_name:
       print_every_house_by_area()
   elif user_input == print_all_by_address_and_cost:
       print_every_house_by_price()
   elif user_input == print_custom:
       #Custom selection
       while True:
           custom_input = int(input(
"""
Please choose from the following:
1. Bedrooms
2. Bathrooms
3. Floors
4. Basement Availability
0. Exit page
"""))
           #bedroom quantity
           if custom_input == bedrooms:
               while True:
                   bedroom_quantity = int(input(
"""
Choose your bedroom quantity.
To get out of the page, please press '0':
"""))
                   if bedroom_quantity == two_bedrooms:
                       print_every_house_with_two_bedrooms()
                   elif bedroom_quantity == three_bedrooms:
                       print_every_house_with_three_bedrooms()
                   elif bedroom_quantity == four_bedrooms:
                       print_every_house_with_four_bedrooms()
                   elif bedroom_quantity == five_bedrooms:
                       print_every_house_with_five_bedrooms()
                   elif bedroom_quantity == six_bedrooms:
                       print_every_house_with_six_bedrooms()
                   elif bedroom_quantity == seven_bedrooms:
                       print_every_house_with_seven_bedrooms()
                   elif bedroom_quantity == quit:
                       break
                   else:
                       print('Sorry, we currently do not have this option. Please come back after!')
               #bathroom quantity
           elif custom_input == bathrooms:
               while True:
                   bathroom_quantity = float(input(
"""
Choose your bathroom quantity.
To get out of the page, please press '0':
"""))
                   if bathroom_quantity == one_bathroom:
                           print_every_house_with_one_bathroom()
                   elif bathroom_quantity == two_bathrooms:
                           print_every_house_with_two_bathrooms()
                   elif bathroom_quantity == two_point_five_bathrooms:
                           print_every_house_with_two_point_five_bathrooms()
                   elif bathroom_quantity == three_bathrooms:
                           print_every_house_with_three_bathrooms()
                   elif bathroom_quantity == four_point_five_bathrooms:
                           print_every_house_with_four_point_five_bathrooms()
                   elif bathroom_quantity == five_bathrooms:
                           print_every_house_with_five_bathrooms()
                   elif bathroom_quantity == ten_bathrooms:
                           print_every_house_with_ten_bathrooms()
                   elif bathroom_quantity == quit:
                           break
                   else:
                       print('Sorry, we currently do not have this option. Please come back after!')
           #floor quantity
           elif custom_input == floors:
               while True:
                   floor_quantity = int(input(
"""
Choose your floor quantity.
To get out of the page, please press '0':
"""))
                   if floor_quantity == one_floor:
                       print_every_house_with_one_floor()
                   elif floor_quantity == two_floors:
                       print_every_house_with_two_floors()
                   elif floor_quantity == three_floors:
                       print_every_house_with_three_floors()
                   elif floor_quantity == four_floors:
                       print_every_house_with_four_floors()
                   elif floor_quantity == quit:
                       break
                   else:
                       print('Sorry, we currently do not have this option. Please come back after!')
           #basement availability
           elif custom_input == basement:
               while True:
                   basement_availability = input(
"""
Choose 'yes' or 'no' for your basement availability.
To get out of the page, please press '0':
""").lower()
                   if basement_availability == yes:
                       print_every_house_with_basement()
                   elif basement_availability == no:
                       print_every_house_without_basement()
                   elif int(basement_availability) == quit:
                       break
                   else:
                       print("You may only choose 'yes' or 'no' for this option, please try again.")
           #To get out of the selection
           elif custom_input == quit:
               break
           #Invalid input message
           else:
               print('Oops, invalid input! Please try again!')
   #break out of code
   elif user_input == quit:
       break
   #unavailable option message
   else:
       print('Oops, this option is not available. Please try another one!')