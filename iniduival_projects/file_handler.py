 #IC 1st worder counter 
# defining the function to view it and calling 0on the path
def view_file(path):
    #try this 
    try:
        #trying to read the path
        file = open(path,"r")
        #print all the coumentws
        print("\ndocument content: ")
        print(file.read())
        #closing the file
        file.close()
        #if the file can't be found then print error 
    except:
        print("file cant be found")
        

#make function to aadd
def add_file(path):
    print("enter text(press double space to stop)")#legit just sstole this from edwing
    lines = []#making an empty list
    #making sure it runs until ill tell it to stop
    while True:
        #defing var
        line = input()
        #making sure it will stop
        if line == "  ":
            break 
        # add lines to line
        lines.append(line)
        #trying again 
    try:
        #adding whatever to the file
        file = open(path,"a")
        #making aloop in line to keep writing
        for line  in lines:
            file.write(line + "\n")
            #close file
        file.close()
        print("content added")
    #if no found then  no work
    except:
        print("file not found womp womp")


#updating file 
def update_file(path):
    try:
        #you rdoing the same thing its not hard
        file = open(path,"r")
        #you can read it but the robot does
        text = file.read()
        #closiung ifle 
        file.close()
        #make it a string
        word_count = len(text.split())
        #the word count
        print("word count;",word_count)
    #expect show user no file
    except:
        print("file not found")
