import sqlite3

#database variable

Database = 'phone.db'

#define print_every_phone to print all phone models
def print_every_phone():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM phone"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their specifications:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Chipset: {phone[2]}") 
            print(f"Max Ram: {phone[3]}")
            print(f"Max SSD: {phone[4]}")
            print(f"Camera MP (Wide and Ultra Wide): {phone[5]}")
            print(f"Screen Resolution: {phone[6]}")
            print(f"Current Operating System: {phone[7]}")
            print(f"Release Year (NZ): {phone[8]}")

def print_every_manufacturer():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM manufacturer;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of manufacturers of selected phone models:")
        for manufacturer in results:
            print(f"Name: {manufacturer[1]}") 

#Main code
while True:
    user_input = input(
"""
What would you like to do?
1. Print all phones
2. Print all manufacturers
3. Quit
""")
    if user_input == "1":
        print_every_phone()
    elif user_input == "2":
        print_every_manufacturer()
    elif user_input == "3":
        break
    else:
        print("Sorry, invalid option!")