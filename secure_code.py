import getpass

USERNAME = "admin"
PASSWORD = "admin123"

username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

if username == USERNAME and password == PASSWORD:
    print("Login Successful")
else:
    print("Invalid Username or Password")