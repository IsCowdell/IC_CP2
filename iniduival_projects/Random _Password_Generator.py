# IC 1st random password generator
#import string 
import string
#import random 
import random




# defining generate password function()
def generate():
#characters = ""
    characters = ""
#  length = ask user How long does the password need to be: 
    length = input("how long does your password have to be: ")

# lower = ask the user does the password need lowercase letters (Y/N):
    lower = input(" does your password need lowercase yes or no: ")
#if yes then += (string.ascii_lowercase) to characters 
    if "yes":
        characters += string.ascii_lowercase
#if else no print you dont want lowercase
    elif "no":
        print(" you dont want lowercase")
# else:
    else:
# show user inccorect vaule
        print("incorrect vaule")
# upppercase = ask the user Does the password need uppercase letters (Y/N):
    uppercase = input("does your password need uppercase yes or no")
#if yes then += (string.ascii_uppercase) to characters 
    if "yes":
        characters += string.ascii_uppercase
  #if else no print you dont want uppercase
    elif "no":
        print(" you dont want uppercase")      
#else:
    else:
#show user incorrect vaule 
        print("incorrect value")
# number = ask the user Does the password need numbers (Y/N):
    number = input(" do you need numbers yes or no")
#if yes then += (string.digits) to characters 
    if "yes":
        characters += string.digits
#if else no print you dont want digits
    elif "no":
        print(" you dont want numbers")  
#else:
    # show user incorrect value
    else:
        print(" show user incorrect value")

#  special_characters = ask the user Does the password need special characters letters (Y/N):
    special_characters = input("Does the password need special characters letters yes or no: ")
#if yes then += (string.punctuation) to characters 
    if "yes":
        characters += string.punctuation
#if else no print you dont want characters
    elif "no":
        print(" you dont want special characters")  
#else:
    # show user incorrect value
    else:
        print(" show user incorrect value")

# generate password 
# for i in range length 
    for i in length:
        password = ""
# password plus equal random. choice(characters )
        password += random.choice(characters)
#print password 
        print(password)
#defining main functions

def main(): 
# show the user Type the number for the action you would like to perform
    choice = input(f" type the number for the action you would like to perform \n 1 is for generate password \n 2 is to quit:1 ")
#1. Generate Passwords
#2. Exit
# if 1 then:
    if choice == "1":
        generate()
# generate password function() 
    #generate_password()
    
# else if 2 then
    elif choice == "2":
        
# exit function 
        exit()
# exit()
# else:
    else:
# show the user incorrect vaule try again
        print(" Incorrect vaule try again")


#defining exit function 
def exit():
# show the user thank you for using my password 
    print(" thank you for using my program good bye")
#quit program
    quit

main()

