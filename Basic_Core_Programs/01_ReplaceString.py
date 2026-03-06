name = input("Enter your name: ")

if len(name) < 3:
    print("Name must have at least 3 characters")
else:
    template = "Hello <<UserName>>, How are you?"
    result = template.replace("<<UserName>>", name)
    print(result)