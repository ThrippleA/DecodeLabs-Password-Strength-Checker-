common_passwords = [
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "password"
]
print("welcome to Decodelabs Password Checker")
password= input("enter your password")
length = len(password)
is_common = password.lower() in common_passwords
print("password recieved succesfully")
print("password length:",length)
if is_common:
    print("Warning: This is a commonly used password")
else:
    print("This password is not in our common password list")
if length < 8:
    print ("password is too short")
else:
    print("password length is allowed")
has_number = False
for character in password:
    if character.isdigit():
        has_number = True
if has_number:
    print("Contains a number: Yes")
else:
    print("Contains a number: No")
has_symbol = False
for character in password:
    if not character.isalnum() and not character.isspace():
        has_symbol = True
if has_symbol:
    print("Contains a symbol: Yes")
else:
    print("Contains a symbol: No")
has_uppercase = False
for character in password:
    if character.isupper():
        has_uppercase = True
if has_uppercase:
    print("Contains uppercase letter: Yes")
else:
    print("Contains uppercase letter: No")
score = 0
if length >= 8:
    score += 1
if has_number:
    score += 1
if has_symbol:
    score += 1
if has_uppercase:
    score += 1
print("Password score:", score)
if is_common:
    print("Password Strength: Weak")
    print("Reason: This password is commonly used")
elif length < 8 or score < 2:
    print("Password Strength: Weak")
elif score < 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")