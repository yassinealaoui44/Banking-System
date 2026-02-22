import json
class user:
    TotalUsers = 0
    def __init__(self, username,email,password,is_admin,balance = 0):
        self.username = username
        self.__email = email
        self.__password = password
        user.TotalUsers += 1
        self.id = user.TotalUsers
        self.isadmin = is_admin # <--- THE FIX
        self.__balance = balance
        
    def get_username(self):
        return self.username
    def get_User_Statue(self):
        return self.is_admin
    def get_balance(self):
        return self.__balance
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__email
    def set_balance(self,amount):
        self.__balance = amount
    def deposit(self,amount):
        try:
            with open("users.json","r") as file:
                 users_list = json.load(file)
        except FileNotFoundError:
                print("Fatal error! Database not found\n")
        for users_dict in users_list:
            if self.id == users_dict["id"]:
                self.__balance += amount
                users_dict["balance"] = self.__balance
                break
        return True   
    def exposit(self,amount):
        try:
            with open("users.json","r") as file:
                 users_list = json.load(file)
        except FileNotFoundError:
                print("Fatal error! Database not found\n")
        for users_dict in users_list:
            if self.id == users_dict["id"]:
                self.__balance -= amount
                users_dict["balance"] = self.__balance
                break
        return True        
    def send_money(self, amount, receiver_id):
        try:
            with open("users.json", "r") as file:
                 users_list = json.load(file)
        except FileNotFoundError:
            print("Fatal Error! Database does not exist.")
            return False
            
        receiver_found = False
        for user_dict in users_list:
            if user_dict["id"] == receiver_id: 
                user_dict["balance"] += amount
                receiver_found = True
                print(f"Success! {user_dict['username']} received the funds.")
                break
                
        if not receiver_found:
            print(f"Transaction Failed: The user with ID '{receiver_id}' does not exist.")
            return False

        self.set_balance(self.get_balance() - amount)
        
        for user_dict in users_list:
            if user_dict["id"] == self.id:
                user_dict["balance"] = self.get_balance()
                break

        with open("users.json", "w") as file:
            json.dump(users_list, file, indent=4)
            
        return True
        
        def deposit(self,balance):
            self.set_balance(self.get_balance() + amount)
            try:
                with open("users.json","r") as file:
                    users_list = json.load(user.json)
            except:
                print("Fatal Error! Database does not exist.")
                return False
            user_found = False
            for users_dict in users_list:
                if users_dict["id"] == self.id:
                   users_dict["balance"] += self.balance
                   user_found = True
            if user_found:
                with open("users.json", "w") as file:
                  json.dump(users_list,file,indent=4)
                  return True
            else:
                print("unexpected error")
                return False
                        
class admin(user):
     def __init__(self, username, email, password,is_admin, balance=0):
        super().__init__(username, email, password,is_admin, balance)
    
def register_new_user(username, email, password, is_admin,balance = 0.0):
    # Step 1: Read the existing data
    try:
        with open("users.json", "r") as file:
            users_list = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, start a new list
        users_list = []

    # Calculate the new ID (Finds the highest current ID and adds 1)
    if len(users_list) > 0:
        new_id = users_list[-1]["id"] + 1
    else:
        new_id = 1

    # Step 2: Translate the data into a dictionary
    # (Notice how this matches the exact structure we built in users.json)
    user_data = {
        "id": new_id,
        "username": username,
        "email": email,
        "password": password, 
        "balance": balance,
        "is_admin": is_admin
    }

    # Step 3: Append the new user to the list in memory
    users_list.append(user_data)

    # Step 4: THE CRITICAL LINE - Write the list back to the JSON file
    with open("users.json", "w") as file:
        json.dump(users_list, file, indent=4) 
        
    print(f"Success! {username} has been registered and saved to the database.")