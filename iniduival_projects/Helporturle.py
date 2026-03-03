# Tell the user you have enter the traignle geneater
#Enter recursion dept(1-5)
# Intake how many depths the user wants and then take that and somehow put it into a recursion
# to make it keep going and going 
# Define the turtle drawing triangle
# 



# def getting mid point whic calling p1 and p2 as a parameter 
# which then return (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) which finds the midpoint 

import turtle


def drawTriangle(points,color,t):
    t.shape("turtle")
    #print a list of colors that the usr can ask for
    #ask user which background color they want 
    #check if colo the usr asked for is in said list
    t.fillcolor(color)
    # drawing the triangle and followign the points
    t.up()
    t.goto(points[0][0],points[0][1])
    t.down()
    t.begin_fill()
    t.goto(points[1][0],points[1][1])
    t.goto(points[2][0],points[2][1])
    t.goto(points[0][0],points[0][1])
    t.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,t):
    #need to make an if loop here chekcing th ecolor to print the triangle correctly
    #also asking the user what color they want 
    colors = ['yellow','blue','green','red','purple']
    colormap = input("What color do you want to choose from(yellow','blue','green','red','purple): ")

    if any(word in colors for word in colormap):

        drawTriangle(points,colormap[degree],t)
        if degree > 0:
            sierpinski([points[0],
                            getMid(points[0], points[1]),
                            getMid(points[0], points[2])],
                    degree-1, t)
            sierpinski([points[1],
                            getMid(points[0], points[1]),
                            getMid(points[1], points[2])],
                    degree-1, t)
            sierpinski([points[2],
                            getMid(points[2], points[1]),
                            getMid(points[0], points[2])],
                    degree-1, t)
    else:
        print("incorrect color go again")
