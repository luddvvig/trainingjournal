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
        choice = input("Write a new log? (W)\nLook at an old log? (R)\nUpdate status? (U)")
        if choice.lower() == "w":
             write_log(name)
        elif choice.lower() == "r":
             "read_log()"
        else:
             print("Use\nWrite a new log? (W)\nLook at an old log? (R)\nUpdate status? (U)")
    else:
        print(f"WARNING!! {name}, you are not authorized!")
        exit_program()

def write_log(name):
     if name.lower() == "ludwig":
          with open("status.txt", "a") as status_file:
               status_file.write(input("Write a short log about todays training here: "))
               status_file.write("\n")
               status_file.write((input("\nHow long was the training? In H here: ")))
               status_file.write("\n")
               status_file.write(input("What was the date of the session? dd/mm/yy"))
               status_file.write("\n")

'''def read_log():

def status():'''

welcome()
