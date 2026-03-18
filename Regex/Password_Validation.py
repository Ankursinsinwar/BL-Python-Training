import re

def password_Validation(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[-_@#$%+])[a-zA-Z0-9-_@#$%+]{8,14}$"
    match = re.match(pattern,password)
    return "Yes" if match else "No"


password = input("Enter your emailpassword : ")
print(password_Validation(password))