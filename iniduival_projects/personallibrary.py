#IC 1st personal library



# Creatiung ewmpty librabry list
library = []
# defining view functions
def view():
    #giving them the option
    print("View:")
    # loop to see if author in library 
    for title, author in library:
        #printing
        print(f"{title} by {author}")
#degfing add function 
def add():
    #creating variables for titl author and adds
    title = input("Title: ")
    author = input("By: ")
    adds = (title, author)
    #showing user thsaat what you have added
    print("you have added")
    #showing variable
    print(f"{title} by {author}")
    #adding to librabry function
    library.append(adds)
#defing the search function 
def search():
    #asking what he wants to search for 
    index = int(input("What would you like to search by? \n 1. Title \n 2. Author"))
    #setting an if statment for if its 1 ask what the user name is 
    if index == 1:
        searchs = input("What is the author's name: ")
        found = False
        #if he finds it he keeps it basically
        for title, author in library:
            if searchs in author:
                found = True
                print(f"{title} by {author}")
    #same thing but this time hes looking for title not author
    elif index ==  2:
        searchs = input("What is the book title: ")
        found = False
        for title, author in library:
            if searchs in title:
                found = True
                print(f"{title} by {author}")
    #can't find it remove it 
    if not found:
        print("No matches found")
# for the function remove if somebody  doesn't like the book they remove it    
def remove():
    for i, (title, author) in enumerate(library, start=1):
        print(f"{i}. {title} by {author}")

    sub = int(input("Enter the number of the item you would like to remove: "))
    #subtract one because the list starts out funny and the first one is zero but user doesn't know that so  this makes it easier
    removed_title, removed_author = library.pop(sub - 1)
    print(f"\nYou have removed {removed_title} by {removed_author}")

    
# all of user interface
def main():
    while True:
        choice = input("Type the number for the action you would like to perform \n 1. View \n 2. Add \n 3. Remove \n 4. Search \n 5. Exit \n")
        if choice == "1":
            view()
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "4":
            search()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
main()