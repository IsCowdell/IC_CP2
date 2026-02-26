#IC 1st main for word counter
#import all of the files 
from file_handler import view_file,add_file,update_file 
#defing main function
def main():
    #asking for file path
    file_path = input("enter the relative file path:")
#making loop to finsih 
    while True:
        #printing everything really neat 
        print("1. update doc info\n 2. view info\n 3 add content\n4.exit" )
       #user has rights again
        choice = input("choose number 1 -4: ")
        #basically this takes whatever they said and calls on the ufnction for whatever they said and they can leave if they want to
        if choice == "1":
            update_file(file_path)
        elif choice == "2":
            view_file(file_path)
        elif choice == "3":
            add_file(file_path)
        elif choice == "4":
            print("why you leave me...")
            break
        else:
            print("invalid choice")

#this is whatever the notes said but i think its saying if the code is right name it runs
if __name__ == "__main__":
    main()