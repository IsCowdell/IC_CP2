


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
#GETTING MID POINT VERY IMPOTANT
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,t,color):
#mkain gusre the traingle hits all the correct points and is right overall
        drawTriangle(points,color,t,degree)
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
 