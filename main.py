
import json
import os
import re
from datetime import datetime
import time

jsonFile = "alarms.json"
import os

def play_alarm_sound():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.system("termux-volume music 15")
    os.system("termux-media-player play alarm.mp3")
#current time
def calender():
   now = datetime.now()
   print("Current Time: ", now.strftime("%H:%M:%S"))
   print("Date: ",now.strftime("%Y-%m-%d"))

if os.path.exists(jsonFile):
        with open (jsonFile,"r") as file: 
          try:
            data = json.load(file)
          except json.JSONDecodeError:
            data = {"username": "", "alarms": []}
else:
    data = {"username": "", "alarms": []}
   
if not data["username"]:
   while True:
      username = input("...Kindly Enter Your Name: ")
      if re.fullmatch(r"[A-Za-z]{3,8}", username):
         data["username"] = username
         break
      else:
         print("username must contain  only letters and be 3 to 8 characters long.")
   with open(jsonFile,"w") as file:
      json.dump(data, file, indent = 4)
   
print(f"Your Alarm Bot Is Ready {data["username"]}")

#watch my alarm
def watch_alarm():
    print("Watching Your Alarms... Will keep repeating when it’s time!")

    current_alarm = None  

    while True:
        now = datetime.now().strftime("%H:%M")

        if os.path.exists(jsonFile):
            with open(jsonFile, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {"username": "", "alarms": []}
        else:
            data = {"username": "", "alarms": []}

        next_alarm = None
        for alarm in data["alarms"]:
            if alarm["set_time"] == now:
                next_alarm = alarm
                break

        if next_alarm and (current_alarm is None or next_alarm != current_alarm):
            current_alarm = next_alarm 
            print(f" Alarm Started: {current_alarm['set_time']} - {current_alarm['set_label']}")

        if current_alarm:
            try:
                 os.chdir(os.path.dirname(os.path.realpath(__file__)))
                 while True:
                    os.system(f'termux-tts-speak -p 0.9 -r 1.3 -l en "{current_alarm["set_label"]}"')
                    play_alarm_sound()
                    stop = input("input Quit to stop alarm...").lower()
                    if stop == "quit":
                      break
            except Exception as tts_error:
                print(f" TTS error: {tts_error}")

            now_check = datetime.now().strftime("%H:%M")
            if now_check != current_alarm["set_time"]:
                print(" Moving to next alarm or waiting for next trigger...")
                current_alarm = None

        time.sleep(1)  
# function for add alarm
def add_alarm():
   if os.path.exists(jsonFile):
      with open (jsonFile,"r") as file:
         try:
            data = json.load(file)
         except json.JSONDecodeError:
             data = {"username": "", "alarms": []}
   else:
        data = {"username": "", "alarms": []}
   while True:
      print("set your alarm below...")
      while True:
          time = input(" Enter your time in 24-hour format (HH:MM): ")
          if re.fullmatch(r"^([01]\d|2[0-3]):([0-5]\d)$", time):
              label = input ("What do you at that moment: ")
              data["alarms"].append({
               "set_time" : time,
              "set_label" : label, 
               })
              break
          else:
              print(" Invalid time. Please use HH:MM format (e.g., 08:30, 14:45)")
      with open(jsonFile,"w") as file:
         json.dump(data , file, indent=4)
         
      print("✅ Alarm Saved") 
      another = input ("Add another alarm ?  (y/n) ").lower()
      if another != "y":
         choose_exit_format = input("Return to main menu  (y/n) ").lower()
         if choose_exit_format == "y":
            print("Returning ...........")
            return
         else:
            print("Exiting ..........") 
            return
# function for remove alarm
def remove_alarm():
    if os.path.exists(jsonFile):
        with open(jsonFile, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {"username": "", "alarms": []}
    else:
        data = {"username": "", "alarms": []}

    if not data["alarms"]:
        print(" There is no alarm here.")
        return

    print("Here are your saved alarms:")
    for i, alarm in enumerate(data["alarms"], start=1):
        print(f"{i}.  {alarm['set_time']} - {alarm['set_label']}")

    try:
        remove = int(input("Enter the number of the alarm to remove: "))
        total = len(data["alarms"])

        if 1 <= remove <= total:
            deleted = data["alarms"].pop(remove - 1)
            print(f" Removed alarm: {deleted['set_time']} - {deleted['set_label']}")
            with open(jsonFile, "w") as file:
                json.dump(data, file, indent=4)
        else:
            print(" Invalid number. Please enter a valid alarm number.")
    except ValueError:
        print(" That is not a number. Please enter a valid number.")
    choose_exit_format = input("Return to main menu  (y/n) ").lower()
    if choose_exit_format == "y":
         print("Returning ...........")
         return
    else:
         print("Exiting ..........") 
         return
# function for view alarm
def view_alarm():
    calender()
    if os.path.exists(jsonFile):
       with open(jsonFile,"r") as  file:
          try:
             data=json.load(file)
          except json.JSONDecodeError:
             data = {"username":"","alarms":[]}
    else:
        data = {"username":"","alarms":[]}
        
    if not data["alarms"]:
         print("There is no alarm here")
    else:
         print("Here are your saved alarm")
         for i,alarms in enumerate(data ["alarms"], start = 1):
            print(f"{i}.  {alarms['set_time']} - {alarms['set_label']}")
            print("Those are the available alarm")
    choose_exit_format = input("Return to main menu  (y/n) ").lower()
    if choose_exit_format == "y":
         print("Returning ...........")
         return
    else:
         print("Exiting ..........") 
         return
# function for exit alarm
def exit_alarm():
    calender()
    print("""Moving out !!!
   Exiting...............""")

# using dictionaries to create option
def main_menu():
   options = { 
       1: "add alarm",
       2: "remove alarm",
       3: "view alarm",
       4: "watch_alarm",
       5: "exit"
   }
   # using loop to go through it 
   for number, needs in options.items():
          print(f"{number} : {needs}")
   while True:
      # using dictionaries to map userinput to each function                   
      choices = {
          1: add_alarm,
          2: remove_alarm,
          3: view_alarm,
          4: watch_alarm,
          5: exit_alarm,
      }
      
      # ask user what they want 
      user_input = input("What do you want : ")
      
      # check if user_input is equal to the function dictionaries
      try:
          userInput = int(user_input)
          if userInput in choices:
                choices[userInput]()
                return
          else:
              print("Enter a valid number !")   
      except ValueError:
          print(" That is not a number ....")
while True:
   main_menu()
   ask = input(" Do you want to return to the main menu? (y/n): ").lower()
   if ask != 'y':
        print(" Goodbye!")
        break
        

   
