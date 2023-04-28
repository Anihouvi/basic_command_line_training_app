import psycopg2
import datetime
from prettytable import PrettyTable
from typing import Tuple, AnyStr, Any, List

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="training",
    user="",
    password=""
)


# Define a function to insert data into the database
def insert_data(date:str, time_trained:float, food_eaten:str,
                food_type:str, calories_intake:int,
                calories_burned:int, weight_loss:float):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO progress \
        (date, time_trained, food_eaten, \
        food_type, calories_intake, \
        calories_burned, weight_loss) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (date, time_trained, food_eaten,
         food_type, calories_intake,
         calories_burned,
         weight_loss)
    )
    conn.commit()


# Define a function to display the records
def display_records():
    cur = conn.cursor()
    cur.execute("SELECT * FROM progress")
    rows = cur.fetchall()
    table = PrettyTable()
    table.field_names = ["ID", "Date",
                         "Time Trained (min)",
                         "Food Eaten",
                         "Food Type",
                         "Calories Intake",
                         "Calories Burned",
                         "Weight Loss (kg)"
                         ]
    for row in rows:
        table.add_row(row)
    print(table)


# Define a function to display the reports
def display_reports(start_date:str, end_date:str):
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date, time_trained, \
        food_eaten, food_type, calories_intake, \
        calories_burned, weight_loss\
         FROM progress WHERE date BETWEEN %s AND %s",
        (start_date, end_date)
    )
    rows = cur.fetchall()
    table = PrettyTable()
    table.field_names = ["ID", "Date",
                         "Time Trained (min)",
                         "Food Eaten",
                         "Food Type",
                         "Calories Intake",
                         "Calories Burned",
                         "Weight Loss (kg)"
                         ]
    for row in rows:
        table.add_row(row)
    print(table)


# Define a function to display the menu
def display_menu():
    table = PrettyTable()
    table.field_names = ["Choice", "Action"]
    table.add_row(["1", "Record Training Data"])
    table.add_row(["2", "View Reports"])
    table.add_row(["3", "Show Entire Table"])
    table.add_row(["4", "Exit"])
    print(table)


# Run the app
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        while True:
            date = input("Enter today's date (YYYY-MM-DD) or type 'b' to go back to the main menu: ")
            if date == "b":
                break
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
                while True:
                    try:
                        time_trained = float(input("Enter the time trained (in minutes): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                food_eaten = input("Enter the food eaten: ")
                food_type = input("Enter the type of food: ")
                while True:
                    try:
                        calories_intake = int(input("Enter the calories intake: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                while True:
                    try:
                        calories_burned = int(input("Enter the calories burned: "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
                while True:
                    try:
                        weight_loss = float(input("Enter the weight loss (in kg): "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                insert_data(date, time_trained, food_eaten, food_type, calories_intake, calories_burned, weight_loss)
                print("Training data recorded successfully.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid date in the format YYYY-MM-DD.")
    elif choice == "2":
        while True:
            start_date = input("Enter the start date (YYYY-MM-DD) or type 'b' to go back to the main menu: ")
            if start_date == "b":
                break
            try:
                datetime.datetime.strptime(start_date, "%Y-%m-%d")
                while True:
                    end_date = input("Enter the end date (YYYY-MM-DD) or type 'b' to go back to the main menu: ")
                    if end_date == "b":
                        break
                    try:
                        datetime.datetime.strptime(end_date, "%Y-%m-%d")
                        display_reports(start_date, end_date)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid date in the format YYYY-MM-DD.")
                if end_date == "b":
                    break
            except ValueError:
                print("Invalid input. Please enter a valid date in the format YYYY-MM-DD.")
    elif choice == "3":
        while True:
            display_records()
            print("Type 'b' to go back to the main menu")
            choice3 = input()
            if choice3 == 'b':
                break
            else:
                print("Invalid input, Please enter 3 to go back to the main menu.")
    elif choice == "4":
        print("Exiting the app...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

