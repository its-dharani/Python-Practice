#Password Checker
password=input("Please Enter your pasword:")
has_number=False
has_Upper=False
for char in password:
    if char.isupper():
        has_Upper=True
    if char.isdigit():
        has_number=True
        
if len(password)>=8 and has_number and has_Upper:
    print("It is a Strong Password")
else:
    print("The password is weak try again")
        