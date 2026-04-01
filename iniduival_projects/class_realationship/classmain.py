#IC 1st Class relationship 
#Starting off the main menu 

#print welcome to the class grade book 
# what do you want to do 
# 1 add new student 
# 2 add grade to student 
# 3 view student record 
# 4 view all students 
# 5 Class sumamary 
# 6 exit
# please enter your choice(1-6) Please only select one of this 
# make an if loop to check if nu,ber is actually in range 
#if not keep bugging them until they make vaild choice 
#


# main.py
# Entry point for the Class Grade Book application.
#
# This file NEEDS TO be THIN remmeber that so like 100 lines or less 
#What we need to do here:
#   1. Import everything needed from helper
#   2. Create the single GradeBook instance
#   3. Run the menu loop until the user chooses Exit



from helperfunctions import (
    GradeBook,
    print_main_menu,
    get_valid_choice,
    menu_add_student,
    menu_add_grade,
    menu_view_student,
    menu_view_all,
    menu_class_summary,
    menu_save_load,
)




def main():

    #Create the GradeBook and loop through the menu.
    #Exits cleanly when the user selects option 7.
    
    gradebook = GradeBook()   # One shared gradebook for the whole session


    # Map each valid menu choice to its action function in helper.py
    actions = {
        "1": menu_add_student,
        "2": menu_add_grade,
        "3": menu_view_student,
        "4": menu_view_all,
        "5": menu_class_summary,
        "6": menu_save_load,
    }


    while True:
        print_main_menu()
        choice = get_valid_choice()


        if choice == "7":
            print("\n Goodbye! Don't forget to save before you go.\n")
            break


        # Look up and call the matching function, passing the gradebook
        actions[choice](gradebook)




main()













































#for class sumary include their names,grades and class average overall
# for the nuermical average make sure to use the data they already gave us