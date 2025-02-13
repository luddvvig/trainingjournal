#TrainingJournal
import datetime
import sys

#For kicking out intruders!
def exit_program():
        print("Program is being shut down")
        sys.exit()

#I need to welcome the user(me)
def welcome():
    time = datetime.date.today()
    formated_date = time.strftime("%m/%d/%y")
    name = input("Enter your name: ")

    if name.lower() == "ludwig":
        print(f"Welcome back {name}!")
        print(f"Today is {formated_date}")
        print("What do you want to do today?")
        choice = input("Write a new log? (W)\nLook at an old log? (NL)\nUpdate status? (U)")
    else:
        print(f"WARNING!! {name}, you are not authorized!")
        exit_program()

def write_log():

def read_log():

def status():

welcome()
