#IC 1st worder counter 
import csv 
#You can do 4 things
print("You can do about 4 things ")
user_chice = input("1 is update document information\n 2 is to view document \n 3 is to add content to document\n 4 is exit the program:").strip()
# 1 is upadte document infor 
#2 is to view document 
#3 is to add content to document 
#4 is exit the program 


file_path = 'iniduival_projects/word_counter.txt'

#add Doncument information would be a function
def 
# defing the upadting doc info 
# with open plce file path and put the mod into "a" for append as fil:
#   variable of writer as = csv.write(file)
#    #write the new row
    # wHAT DO YOU WANT TO ADD  # Ask user for input for a new row
    # The inputs are stored in variables
    #value1 = input("Enter column 1 data: ")
   ## value2 = input("Enter column 2 data: ")
    #value3 = input("Enter column 3 data: ")
    
    # Create a list with the new data
   # new_row = [value1, value2, value3]



#viewing doc information would be a function
def viewing(): 

    try: 
        # with open plce file path and put the mod into "r" for reading as fil: 
        with open(file_path,mode = 'r') as file:
        #   variable of reader as = csv.read(file)
            reader = file.read()
        #    #make sure to have them read every single row
        for row in reader:
            print(row)
    except ValueError:
        print("File not found")
        return

#To exit the program 
def exit():
# show the user goodbye!
    print("Goodbye!?!")
# break out of program 
    quit
