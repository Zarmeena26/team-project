def login(username, password):
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Login Failed")

login("admin","1234")