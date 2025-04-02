import sqlite3

Database = 'cars.db'

def print_every_car():
    speed = input("What car speed?: ")
    with sqlite3.connect(Database) as db:
        cursor = db.cursor()
        sql = "SELECT name,top_speed,horsepower FROM cars WHERE top_speed > ?"
        cursor.execute(sql,(speed,))
        results = cursor.fetchall()

        #print them nicely
        print("The following are the list of chosen cars and their specifications:")
        for car in results:
            print(f"Name: {car[0]}") 
            print(f"Top Speed: {car[1]}") 
            print(f"Horsepower: {car[2]}")

if __name__ == "__main__":
    print_every_car()