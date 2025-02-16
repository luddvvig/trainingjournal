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
     return name, formated_date

def main_menu(name, formated_date):
     while True:
          if name.lower() == "ludwig":
               print(f"Welcome back {name}!")
               print(f"Today is {formated_date}")
               print("What do you want to do today?")
               choice = input("Write a new log? (W)\nLook at an old log? (R)\nUpdate status? (U)\nQuit? (Q) ")
               if choice.lower() == "w":
                    write_log(name)
                    continue
               elif choice.lower() == "r":
                    read_log()
               elif choice.lower() == "q":
                    exit_program()
               else:
                    print("Invald input, try again!")
                    print("Use\nWrite a new log? (W)\nLook at an old log? (R)\nUpdate status? (U)")
          else:
               print(f"WARNING!! {name}, you are not authorized!")
               exit_program()

def write_log(name):
     with open("status.txt", "a") as log_file:
          log_file.write("\n")
          log_file.write(input("What was the date of the session? dd/mm/yy: "))
          log_file.write("\n")
          log_file.write(input("Write a short log about todays training here: "))
          log_file.write("\n")
          log_file.write((input("\nHow long was the training? In H here: ")))
          log_file.write("\n")
          log_file.write(f"{name}")
          log_file.write("\n")
          
          
def read_log():
     date = input("What date do you want to check out? (dd/mm/yy): ")
     with open("status.txt", "r") as file:
          lines = file.readlines()
          nmr_line = -1  

          for i, row in enumerate(lines):  
               if date in row: 
                    nmr_line = i
                    break 

          if nmr_line != -1:
               
               for i in range(nmr_line, min(nmr_line + 3, len(lines))):
                    print(lines[i].strip())
          else:
               print(f"No log found for date: {date}")

#def status():
def main():
     name, formated_date = welcome()
     main_menu(name, formated_date)

if __name__ == "__main__":
     main()
