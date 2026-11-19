DecodeLabs Password Checker
Project Overview
The Password Checker is a beginner-friendly cybersecurity project developed using Python.
It evaluates a user's password based on specific security criteria and classifies it as Weak, Medium, or Strong.
The project demonstrates basic Python programming concepts and introduces the importance of creating stronger passwords for better account security.

 Key Features
The program checks passwords against four main criteria:
Length: Checks whether the password contains at least 8 characters.
Checks for at least one numerical digit.
Special Characters:Checks for symbols such as @, #, $, and !.
Uppercase Letters: Checks whether the password contains at least one uppercase letter.

Password Strength Classification

Based on the number of criteria met, the program classifies passwords as:
Weak: Fewer than 2 criteria met.
Medium: 2 or 3 criteria met.
Strong: All 4 criteria met.

 Requirements
Python 3.x
How to Run the Project

1. Clone this repository:
   git clone https://github.com/ThrippleA/DecodeLabs-Password-Checker-.git
2. Navigate to the project folder:
   cd DecodeLabs-Password-Checker-
3. Run the Python program:
   python "password checker.py"
4. Enter a password when prompted to see its strength rating.

Sample Test Results
 Password          Strength
donman               Weak 
Donman12            Medium 
Donman@123          Strong 
DONMAN123           Medium 
12345678             Medium 

Application Used
 Python 3
 Visual Studio Code
 Git and GitHub

Lesson Learned:
Through this project, I practised:
 Python conditional statements.
Loops and string methods.
Boolean variables.
User input and output.
Basic password security assessment.
Version control using Git and GitHub.

Disclaimer
This project is an educational password-strength checker. Its scoring system is simplified and should not be treated as a complete measure of real-world password security.