import itertools

#Assignment: Python Strings

#1. Product Review Analysis

#Task 1: Keyword Highlighter

"""Pseudocode - 
Step 1 - use split() to separate reviews.  
Step 2 - 
Step 3 - use the if...in loop to search for key words.  
Step 4 - use upper() to capitalize key words
Step 5 - """

reviews = ["This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]


"""def review_list(review_string):
    rev_stringa = []
    for words in review_string:
        if words == "good":
            words.upper()
            rev_stringa.append(words)
        elif words == "excellent":
            review_string[words].replace("excellent", "EXCELLENT")
            rev_stringa.append(words)
        elif words == "bad":
            review_string[words].replace("bad", "BAD")
            rev_stringa.append(words)
        elif words == "poor":
            review_string[words].replace("poor", "POOR")
            rev_stringa.append(words)
        elif words == "average":
            review_string[words].replace("average", "AVERAGE")
            rev_stringa.append(words)
        else:
            rev_stringa.append(words)
    print(rev_stringa)
"""
for i in reviews:
    print(i)

"""delimiter = ','

for i in range(len(reviews)):
    review_string = delimiter.join(reviews)
print(review_string)"""

#review_list(review_string)

#2.  User Input Data Processor

#Task 1: Input Length Validator

def check_name():
    first_name = input("Enter a first name at least 2 letters long: ")
    last_name = input("Enter a last name at least 2 letters long: ")

    if len(first_name) > 1 and len(last_name) > 1:
        print(f"First name is {len(first_name)} characters long. ")
        print(f"Last name is {len(last_name)} characters long. ")
    else:
        print(f"One or more of your names are not at least 2 characters long. ")

check_name()

#Task 2: Password Complexity Checker

def password_checker():
    counter = 0
    print("Let's create a password. ")
    print("It must have at least 8 characters, one upper case and 1 number in it.")
    user_pwd = input("Enter a password: ")
    for char in user_pwd:
        if len(user_pwd) < 7:
            print("Password is not at least 8 characters long.")
        if char.isdigit() > 1 and char.isupper > 1:
            continue
        else:
            counter +=1
    if counter > 0:    
        print(f"{user_pwd} is not acceptable.")
        print("All passwords should be at least 8 chars long, ")
        print("with the minimum of 1 uppercase letter and 1 number.")

password_checker()

#Task 3. Email Formatter

print("Let's check the email formats.")

def eformchecker():
    count = 0
    item = 0
    print("Rules for email format are below: ")
    print("Email prefixes must be between 5 to 15 characters long, ")
    print("Emails can only have alpha characters, with only 1 optional character.")
    print("The email domain will always be @colematron.com")

    user_email = input("Enter your unique email prefix: ")
    for char in user_email:
        if char.isdigit():
            item += 1
        elif char.isalpha:
            count += 1
    if item >= 1:
        print(f"Email prefix {user_email} is not acceptable.  Too many non-alpha characters in it.")
    else:
        print(f"Email {user_email}@colematron.com is acceptable.")
        
eformchecker()

#3. Interactive Help Desk Bot

#Task 1: Command Parser

def help_choices():
    user_input = input("Enter a command: ")
    for word in user_input:
        while user_input != " ":
            if word == "help" or word == "issue":
                print("From your input, you need some type of help.")
                help_input = input("What is your specific need?  Keep it within two words.")
                print(f"I see you need help with {help_input}, I will direct your issue to the appropriate staff.")
            elif word == "support" or word == "customer service":
                print("Please hold on while I transfer you to customer service.")
            else:
                print("There is no issue here.  This helpdesk issue will end.  Have a nice day!")
    print("Your call has been completed.  Have a nice day!")

help_choices()




