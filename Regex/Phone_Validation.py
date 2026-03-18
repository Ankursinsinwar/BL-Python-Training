import re

def phoneNo_Validation(phoneNo):
    pattern = "[6-9][0-9]{9}"
    match = re.match(pattern,PhoneNo)
    return "Yes" if match else "No"

PhoneNo = input("Enter your phone number : ")
print(phoneNo_Validation(PhoneNo))

