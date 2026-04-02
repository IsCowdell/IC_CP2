from helperfunctions import GradeBook, Menu
 
# create the gradebook and menu then start the program
gradebook = GradeBook()
menu = Menu(gradebook)
menu.run()