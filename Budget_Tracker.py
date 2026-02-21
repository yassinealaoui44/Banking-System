from users import user
import users
import time
import re
import json
import os
print("===============================BUDGET TRACKER===============================")
print("1. Sign-up\n")
print("2. Login\n")
print("3. Close application\n")

def is_valid_email(email):
    # This pattern translates to: 
    # [some letters/numbers] @ [some letters/numbers] . [some letters]
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # re.match() compares your string against the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

while True:
    try:
        choice = int(input("\nPlease select an option (1-3): \n"))
        
        if 1 <= choice <= 3:
            break 
        else:
            print("Invalid choice: Please choose a number between 1 and 3.\n")
            
    except ValueError:
        print("Invalid input: That is not a number. Please enter 1, 2, or 3.\n")

print(f"\nProceeding with option {choice}...\n")
print("\nLoading", end="\n") 

for _ in range(3):
    time.sleep(0.6)       
    print(".", end="", flush=True) 

time.sleep(0.2)          
print("\n")

is_loggedIN = False

if choice == 1:
    print("Enter username : \n")
    username = input()
    while True:
         email = input("Enter your email: \n")
    
         if is_valid_email(email):
           break 
         else:
             print("Error: Invalid email format. Please try again (e.g., name@email.com). \n")
    print("Enter Password : \n")
    password = input()
    ObjUser = user(username,email,password)
    users.register_new_user(username,email,password)
if choice == 2:
    print("Enter your username : \n") 
    username = input()
    print("Enter your password")
    password = input()
    try:
        with open("users.json", "r") as file:
            users_list = json.load(file)
    except FileNotFoundError:
        print("Database does not exist.\n") 

    for user_dict in users_list:
        if user_dict["username"] == username:
            if user_dict["password"] == password:
                print(f"Login successful! Welcome back, {username}.\n")
                is_loggedIN = True
                ObjUser = user(user_dict["username"],user_dict["email"],user_dict["is_admin"],user_dict["balance"])
                
            else:
                print("Error: Incorrect password.\n")           
                
    
if choice == 3:
    exit

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
if is_loggedIN:
    clear_screen()
    #check if the user is an admin or not
    print("Welcome! {username}\n")
    print("=============================== MENU ===============================")
    print("1. Check Balance \n")
    print("2. Deposit Money \n")
    print("3. Exposit \n")
    print("4. Make a Transaction \n")
    
    
    
