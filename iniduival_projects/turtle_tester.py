

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
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']

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

def main():
   depth = input("what depth do you want(1-5) please:")
   depthnum = int(depth)
   t = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,depthnum,t)
   myWin.exitonclick()

main()
