import re

data = '''my name is Ankur 
contact on my email ankur@gmail.com 
or abc@biz.com. Call on 8011349068.'''


emails = re.findall("[a-zA-Z0-9]+@[a-zA-Z0-9.]+\\.[a-z]{2,}", data)
print(f"Emails found: {emails}") 


phone_match = re.search("[6-9][0-9]{9}", data)
if phone_match:
    print(f"First Phone: {phone_match.group()} at index {phone_match.start()}")


pattern = re.compile("Ankur")
if pattern.search(data):
    print(f"Pattern {pattern.pattern} was found using a compiled object.")
