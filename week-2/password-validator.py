password = input("Enter the password: ");

if(len(password) < 8):
    print("Password should be at least 8 characters long");

hasUppercase = False;
hasLowercase = False;
hasDigit = False;
hasSpecialChar = False;

for char in password:
    if char.isupper():
        hasUppercase = True;
    elif char.islower():
        hasLowercase = True;
    elif char.isdigit():
        hasDigit = True;
    elif char in "!@#$%^&*()":
        hasSpecialChar = True;

if not hasUppercase:
    print("Password should contain at least one uppercase letter")
if not hasLowercase:
    print("Password should contain at least one lowercase letter")
if not hasDigit:
    print("Password should contain at least one digit")
if not hasSpecialChar:
    print("Password should contain at least one special character (!@#$%^&*())")   

if (
    len(password) >= 8
    and hasUppercase
    and hasLowercase
    and hasDigit
    and hasSpecialChar
):
    print("Password is valid!")