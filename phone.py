import sqlite3

#database variable

Database = 'phone.db'

#define print_every_phone to print all phone models
def print_every_phone():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from phone
        #print them nicely
        print("The following are the list of some current phone models with their specifications:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Chipset: {phone[2]}") 
            print(f"Max RAM: {phone[3]}")
            print(f"Max SSD: {phone[4]}")
            print(f"Camera MP (Wide and Ultra Wide): {phone[5]}")
            print(f"Screen Resolution: {phone[6]}")
            print(f"Current Operating System: {phone[7]}")
            print(f"Release Year (NZ): {phone[8]}")

#define print_every_phone to print all phone model names
def print_every_phone_name():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT name FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from phone
        #print them nicely
        print("The following are the list of some current phone models with their names:")
        for phone in results:
            print(f"Name: {phone[1]}") 

#define print_every_phone to print all phone model chipsets
def print_every_phone_chipset():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT chip FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from phone
        #print them nicely
        print("The following are the list of some current phone models with their chipsets:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Chipset: {phone[2]}") 

#define print_every_phone to print all phone model max RAMs
def print_every_phone_ram():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT max_RAM FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their specifications:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Max RAM: {phone[3]}")

#define print_every_phone to print all phone model max SSDs
def print_every_phone_ssd():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their specifications:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Max SSD: {phone[4]}")

#define print_every_phone to print all phone model camera megapixels
def print_every_phone_camera_mp():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT camera_mp_wide_and_ultra_wide FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their camera megapixels:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Camera MP (Wide and Ultra Wide): {phone[5]}")

#define print_every_phone to print all phone model display resolutions
def print_every_phone_screen_res():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT display_res FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their screen resolutions:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Screen Resolution: {phone[6]}")

#define print_every_phone to print all phone model current operating systems
def print_every_phone_current_os():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT current_os FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their current operating system:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Current Operating System: {phone[7]}")

#define print_every_phone to print all phone model release years
def print_every_phone_release_year_nz():
    '''print all the products nicely'''
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT nz_release_year FROM phone;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #loop through all the results from products
        #print them nicely
        print("The following are the list of some current phone models with their release year:")
        for phone in results:
            print(f"Name: {phone[1]}") 
            print(f"Release Year (NZ): {phone[8]}")

#define print_every_manufacturer to print all manufacturers
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
2. Prine all phone names only
3. Prine all phone names and chipsets only
4. Prine all phone names and max RAM only
5. Prine all phone names and max SSD only
6. Prine all phone names and Camera MP (Wide and Ultra Wide) only
7. Prine all phone names and screen resolution only
8. Prine all phone names and current OS only
9. Prine all phone names and release year (NZ) only
10. Print all manufacturers
11. Quit
""")
    if user_input == "1":
        print_every_phone()
    elif user_input == "2":
        print_every_phone_name()
    elif user_input == "3":
        print_every_phone_chipset()
    elif user_input == "4":
        print_every_phone_ram()
    elif user_input == "5":
        print_every_phone_ssd()
    elif user_input == "6":
        print_every_phone_camera_mp()
    elif user_input == "7":
        print_every_phone_screen_res()
    elif user_input == "8":
        print_every_phone_current_os()
    elif user_input == "9":
        print_every_phone_release_year_nz()
    elif user_input == "10":
        print_every_manufacturer()
    elif user_input == "11":
        break
    else:
        print("Sorry, invalid option!")