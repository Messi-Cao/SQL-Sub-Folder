import sqlite3

#database variable

Database = 'cars.db'

#define print_every_car to print all car models
def print_every_car():
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT * FROM cars"
        cursor.execute(sql)
        results = cursor.fetchall()

        #print them nicely
        print("The following are the list of chosen cars and their specifications:")
        for car in results:
            print(f"Name: {car[1]}") 
            print(f"Top Speed: {car[2]}") 
            print(f"Horsepower: {car[3]}")

if __name__ == "__main__":
    print_every_car()