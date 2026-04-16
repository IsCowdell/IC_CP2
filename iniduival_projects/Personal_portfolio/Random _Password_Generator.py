# IC 1st random password generator
#import string 
import string
#import random
import random

# Functions for the different password requirements
def get_user_requirements():
    # creating an empty string
    characters = ""
    
    # length = ask user How long does the password need to be: 
    length = int(input("How long does your password have to be: "))

    # lower = ask the user does the password need lowercase letters (Y/N):
    lower = input("Does your password need lowercase (yes/no): ").lower()
    # if yes then += add lowercase to characters 
    if lower == "yes":
        characters += string.ascii_lowercase

    # upppercase = ask the user Does the password need uppercase letters (Y/N):
    uppercase = input("Does your password need uppercase (yes/no): ").lower()
    # if yes then += add uppercase to characters 
    if uppercase == "yes":
        characters += string.ascii_uppercase

    # number = ask the user Does the password need numbers (Y/N):
    number = input("Do you need numbers (yes/no): ").lower()
    # if yes then += add digits to characters 
    if number == "yes":
        characters += string.digits

    # special_characters = ask the user Does the password need special characters letters (Y/N):
    special = input("Does the password need special characters (yes/no): ").lower()
    # if yes then += add special characters to characters 
    if special == "yes":
        characters += string.punctuation
        
    return length, characters

# A function that makes the password once it is the correct length
def assemble_password(length, characters):
    options = []
        # Loop 4 times to create four different options
    for selection in range(4):
            # generate password 
            password = ""
            # for i in range length 
            for i in range(length):
                # password plus equal random. choice(characters)
                password += random.choice(characters)
            options.append(password)
    
    return options

# A main function that runs the code
def main():
    # show the user Type the number for the action you would like to perform
    print("Password Generator")
    print("1. Generate Password")
    print("2. Exit")
    #giving the user rights
    choice = input("Type the number for the action you would like to perform: ")

    # if 1 then:
    if choice == "1":
        # Call the requirements function
        pass_length, char_pool = get_user_requirements()
        
        # Call the assembly function
        password_list = assemble_password(pass_length, char_pool)
        #printing the passwords in different lines
        print("\nHere are your 4 password options")
        for password in password_list:
            print("-" + password)
        
        # Loop back to start
        main()

    # else if 2 then
    elif choice == "2":
        # show the user thank you for using my password 
        print("Thank you for using my program. Goodbye!")
    
    # else: show user incorrect vaule try again
    else:
        print("Incorrect value, try again.")
        main()

# Run the program
main()

