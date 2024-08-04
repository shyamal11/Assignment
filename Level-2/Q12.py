def login():
    username = input("Enter username: ")
    
    for attempt in range(3):
        password = input("Enter password: ")
        retype_password = input("Re-type password: ")
        
        if password == retype_password:
            print("Password confirmed. Login successful.")
            return
        else:
            print("Passwords do not match. Try again.")
    
    print("Failed to confirm password after 3 attempts.")

login()
