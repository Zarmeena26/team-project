def login(username, password):
    # Basic validation check
    if not username or not password:
        print("Please enter both username and password")
        return

    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Login Failed")

login("admin","1234")
