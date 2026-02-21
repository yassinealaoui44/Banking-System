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
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
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
def delete_user(target_id):
    try:
        with open("users.json", "r") as file:
            users_list = json.load(file)
    except FileNotFoundError:
        print("Error: Database does not exist.\n")
        return False

    user_deleted = False
    
    for i in range(len(users_list)):
        if users_list[i]["id"] == target_id:
            del users_list[i]
            user_deleted = True
            break

    if user_deleted:
        with open("users.json", "w") as file:
            json.dump(users_list, file, indent=4)
        print(f"Success! User with ID {target_id} has been permanently deleted.\n")
        return True
    else:
        print(f"Error: Could not find a user with ID {target_id}.\n")
        return False
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
if is_loggedIN:
    clear_screen()
    #check if the user is an admin or not
    if ObjUser.get_User_Statue():
       print("ADMIN PANEL\n")
       print("Welcome! {username}\n")
       print("=============================== MENU ===============================")
       print("1. Track users \n")
       print("2. Exit")
       secChoice = int(input())
       if secChoice == 1:
           print("Users : \n")
           try:
               with open("users.json", "r") as file:
                   users_list = json.load(file)
           except FileNotFoundError:
               print("Fatal Error, Database does not exist\n")
               exit
           i = 0
           for user_dict in users_list:
               print("User {i} \n")
               print("Username : ",user_dict["username"],"\n")
               print("Email : ",user_dict["email"],"\n")
               print("Password : ", user_dict["password"],"\n")
               print("Balance : ", user_dict["balance"],"\n")
           print("1. Add User\n")
           print("2. Modify a user\n")
           print("3. Delete a user\n")
           while True:
              try:
                 adminChoice = int(input("\nPlease select an option (1-3): \n"))
        
                 if 1 <= adminChoice <= 3:
                    break 
                 else:
                       print("Invalid choice: Please choose a number between 1 and 3.\n")
            
              except ValueError:
                    print("Invalid input: That is not a number. Please enter 1, 2, or 3.\n")
           if adminChoice == 1:
               usernamed = input()
               emailed = input()
               passworded = input()
               balanced = float(input())
               users.register_new_user(usernamed,emailed,passworded,balanced)
           if adminChoice == 2:
               try:
                   with open("users.json","r") as file:
                       users_list = json.load(file)
               except FileNotFoundError:
                   print("Fatal Error! Database does not exist \n")
                   exit
               print("Enter the user's id to proceed \n")
               id_admin_input = int(input())
               for users_dict in users_list:
                   if id_admin_input == user_dict["id"]:
                       print("user found\n")
                       print("Username : ",user_dict["username"],"\n")
                       print("Email : ",user_dict["email"],"\n")
                       print("Password : ", user_dict["password"],"\n")
                       print("Balance : ", user_dict["balance"],"\n")
                       print("1. Modify Username.\n")
                       print("2. Modify Email.\n")
                       print("3. Modify Password.\n")
                       print("4. Modify Balance. \n")
                       while True:
                           try:
                              crudChoice = int(input())
                              
                              if 1 <= crudChoice <= 4:
                                  break
                              else:
                                  print("Invalid choice: Please choose a number between 1 and 3.\n")
                           except ValueError:
                               print("Invalid input: That is not a number. Please enter 1, 2, or 3.\n")
                               
                       if crudChoice == 1:
                           print("Enter new username\n")
                           user_dict["username"] = input()
                       if crudChoice == 2:
                           print("Enter new email\n")
                           user_dict["email"] = input()
                       if crudChoice == 3:
                           print("Enter new password\n")
                           user_dict["password"] = input()
                       if crudChoice == 4:
                           print("Enter new balance\n")
                           user_dict["balance"] = float(input())
                       break
           if adminChoice == 3:
                print("Enter id\n")
                delete_id = int(input())
                is_deleted = delete_user(delete_id)
                if is_deleted:
                    print("User deleted succesfully\n")
                else:
                    print("User not found.")
                    
                
                   
                           
                           
                       
            
                   
               
               
       
    
    
