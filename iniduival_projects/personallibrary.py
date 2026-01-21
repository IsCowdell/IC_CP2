library = []

def view():
    print("View:")
    for title, author in library:
        print(f"{title} by {author}")

def add():
    title = input("Title: ")
    author = input("By: ")
    adds = (title, author)
    print("you have added")
    print(adds)
    library.append(adds)

def search():
    index = int(input("What would you like to search by? \n 1. Title \n 2. Author"))
    if index == 1:
        searchs = input("What is the author's name: ")
        found = False
        for title, author in library:
            if searchs in author:
                found = True
                print(f"{title} by {author}")

    elif index ==  2:
        searchs = input("What is the book title: ")
        found = False
        for title, author in library:
            if searchs in title:
                found = True
                print(f"{title} by {author}")

    if not found:
        print("No matches found")
    
def remove():
    for i, (title, author) in enumerate(library, start=1):
        print(f"{i}. {title} by {author}")

    sub = int(input("Enter the number of the item you would like to remove: "))
    removed_title, removed_author = library.pop(sub - 1)
    print(f"\nYou have removed {removed_title} by {removed_author}")

    

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
