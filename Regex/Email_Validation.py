import re

def email_Validation(email):
    pattern = "[a-zA-Z0-9]+@[gmail]+\\.[com]"
    match = re.match(pattern,email)
    return "Yes" if match else "No" 


Email = input("Enter your email : ")
print(email_Validation(Email))