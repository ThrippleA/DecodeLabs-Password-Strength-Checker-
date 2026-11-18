print("welcome to Decodelabs Password Checker")
password= input("enter your password")
length = len(password)
print("password recieved succesfully")
print("password length:",length)
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
    if not character.isalnum():
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
if score < 2:
    print("Password Strength: Weak")
elif score < 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")