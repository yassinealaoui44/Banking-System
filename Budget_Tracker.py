from users import user
import users
import time
import re
import json
import os

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

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

while True:
    clear_screen()
    print("===============================BUDGET TRACKER===============================")
    print("1. Sign-up\n")
    print("2. Login\n")
    print("3. Close application\n")

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
    print("\nLoading", end="") 
    for _ in range(3):
        time.sleep(0.6)       
        print(".", end="", flush=True) 
    time.sleep(0.2)          
    print("\n")

    is_loggedIN = False
    ObjUser = None

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
        users.register_new_user(username, email, password, False)
        time.sleep(2) 

    elif choice == 2:
        print("Enter your username : \n") 
        username = input()
        print("Enter your password: \n")
        password = input()
        isadmin = False
        try:
            with open("users.json", "r") as file:
                users_list = json.load(file)
                
            for user_dict in users_list:
                if user_dict["username"] == username:
                    if user_dict["password"] == password:
                        print(f"Login successful! Welcome back, {username}.\n")
                        is_loggedIN = True
                        if user_dict["username"] == "Groot" and user_dict["password"] == "groot1234":
                            isadmin = True
                        ObjUser = user(user_dict["username"], user_dict["email"], user_dict["password"], isadmin, user_dict["balance"])
                        time.sleep(1.5)
                        break
                    else:
                        print("Error: Incorrect password.\n")           
                        time.sleep(1.5)
                        
            if not is_loggedIN:
                print("User not found or incorrect credentials.\n")
                time.sleep(1.5)
                
        except FileNotFoundError:
            print("Database does not exist.\n")
            time.sleep(1.5)

    elif choice == 3:
        print("Closing application. Goodbye!")
        exit()

    if is_loggedIN:
        while True:
            clear_screen()
            
            if ObjUser.isadmin: 
                print("ADMIN PANEL\n")
                print(f"Welcome! {ObjUser.username}\n")
                print("=============================== MENU ===============================")
                print("1. Manage Users \n")
                print("2. Logout\n")
                
                try:
                    secChoice = int(input())
                except ValueError:
                    continue
                    
                if secChoice == 1:
                    print("Users : \n")
                    try:
                        with open("users.json", "r") as file:
                            users_list = json.load(file)
                    except FileNotFoundError:
                        print("Fatal Error, Database does not exist\n")
                        continue
                        
                    for user_dict in users_list:
                        print(f"User ID: {user_dict['id']}")
                        print("Username : ", user_dict["username"])
                        print("Email : ", user_dict["email"])
                        print("Password : ", user_dict["password"])
                        print("Balance : ", user_dict["balance"], "\n")
                        
                    print("1. Add User\n")
                    print("2. Modify a user\n")
                    print("3. Delete a user\n")
                    print("4. Back to Admin Menu\n")
                    
                    while True:
                        try:
                            adminChoice = int(input("\nPlease select an option (1-4): \n"))
                            if 1 <= adminChoice <= 4:
                                break 
                            else:
                                print("Invalid choice: Please choose a number between 1 and 4.\n")
                        except ValueError:
                            print("Invalid input: That is not a number. Please enter a valid option.\n")
                            
                    if adminChoice == 1:
                        print("Enter new username\n")
                        usernamed = input()
                        print("Enter new email\n")
                        emailed = input()
                        print("Enter new password\n")
                        passworded = input()
                        print("Enter starting balance\n")
                        try:
                            balanced = float(input())
                        except ValueError:
                            balanced = 0.0
                        users.register_new_user(usernamed, emailed, passworded, False, balanced)
                        input("\nPress Enter to continue...")
                        
                    elif adminChoice == 2:
                        try:
                            with open("users.json","r") as file:
                                users_list = json.load(file)
                        except FileNotFoundError:
                            print("Fatal Error! Database does not exist \n")
                            continue
                            
                        print("Enter the user's id to proceed \n")
                        try:
                            id_admin_input = int(input())
                        except ValueError:
                            print("Invalid ID.\n")
                            continue
                            
                        user_found_for_edit = False
                        for user_dict in users_list:
                            if id_admin_input == user_dict["id"]:
                                user_found_for_edit = True
                                print("User found\n")
                                print("Username : ", user_dict["username"])
                                print("Email : ", user_dict["email"])
                                print("Password : ", user_dict["password"])
                                print("Balance : ", user_dict["balance"], "\n")
                                
                                print("1. Modify Username\n")
                                print("2. Modify Email\n")
                                print("3. Modify Password\n")
                                print("4. Modify Balance\n")
                                
                                while True:
                                    try:
                                        crudChoice = int(input())
                                        if 1 <= crudChoice <= 4:
                                            break
                                        else:
                                            print("Invalid choice: Please choose between 1 and 4.\n")
                                    except ValueError:
                                        print("Invalid input.\n")
                                        
                                if crudChoice == 1:
                                    print("Enter new username\n")
                                    user_dict["username"] = input()
                                elif crudChoice == 2:
                                    print("Enter new email\n")
                                    user_dict["email"] = input()
                                elif crudChoice == 3:
                                    print("Enter new password\n")
                                    user_dict["password"] = input()
                                elif crudChoice == 4:
                                    print("Enter new balance\n")
                                    try:
                                        user_dict["balance"] = float(input())
                                    except ValueError:
                                        print("Invalid balance.\n")
                                        
                                with open("users.json", "w") as file:
                                    json.dump(users_list, file, indent=4)
                                print("User modified successfully!\n")
                                break
                                
                        if not user_found_for_edit:
                            print("User ID not found.\n")
                        input("\nPress Enter to continue...")
                                
                    elif adminChoice == 3:
                        print("Enter id to delete\n")
                        try:
                            delete_id = int(input())
                            delete_user(delete_id)
                        except ValueError:
                            print("Invalid ID format.\n")
                        input("\nPress Enter to continue...")
                    elif adminChoice == 4:
                        print("Returning to Admin Menu...")
                        time.sleep(1)
                elif secChoice == 2:
                    print("Logging out...")
                    time.sleep(1)
                    is_loggedIN = False
                    break 
                    
            else:   
                print("===============================BUDGET TRACKER===============================")
                print(f"Welcome! {ObjUser.username}\n")
                print("1. Check balance\n")
                print("2. Make a deposit\n")
                print("3. Make an exposit\n")
                print("4. Make a transaction\n")
                print("5. Logout")
                
                while True:
                    try:
                        userChoice = int(input("\nPlease select an option (1-5): \n"))
                        if 1 <= userChoice <= 5:
                           break
                        else:
                           print("Invalid choice please try again\n")
                    except ValueError:
                        print("Choice not valid\n")
                        
                if userChoice == 1:
                    print("Your balance is : ", ObjUser.get_balance(), "\n")
                    input("Press Enter to continue...")
                    
                elif userChoice == 2:
                    print("How much would you like to deposit \n")
                    while True:
                        try:         
                           deposit_balance = float(input())
                           if deposit_balance > 0:
                               break
                           else:
                               print("Amount must be greater than 0, please try again\n")
                        except ValueError:
                            print("Invalid input form\n")
                            
                    if ObjUser.deposit(deposit_balance):
                        print("Deposit done successfully\n")
                        print("Your balance is : ", ObjUser.get_balance())
                    else:
                        print("Unexpected error\n")
                    input("Press Enter to continue...")
                        
                elif userChoice == 3:
                    print("Enter Exposit value\n")
                    while True:
                        try:
                            expositValue = float(input())
                            if 0 <= expositValue <= ObjUser.get_balance():
                              break
                            else: 
                                print("Exposit value must be positive and not exceed your balance\n")
                        except ValueError:
                            print("Try again please\n")
                            
                    if ObjUser.exposit(expositValue):
                        print("Exposit done successfully\n")
                        print("Your balance is : ", ObjUser.get_balance())
                    input("Press Enter to continue...")
                        
                elif userChoice == 4:
                    print("Enter the id of the receiver of your money\n")
                    try:
                        receiver_id = int(input()) 
                        print("Enter the amount you want to send \n")
                        while True:
                            try:
                                amount_sent = float(input())
                                if 0 <= amount_sent <= ObjUser.get_balance():
                                    break
                                else:
                                    print("Invalid amount\n")
                            except ValueError:
                                print("Try again please\n")
                                
                        if ObjUser.send_money(amount_sent, receiver_id):
                          print("Amount sent successfully\n")
                    except ValueError:
                        print("Invalid ID.\n")
                    input("Press Enter to continue...")
                      
                elif userChoice == 5:
                    print("Logging out securely...")
                    time.sleep(1)
                    is_loggedIN = False 
                    break