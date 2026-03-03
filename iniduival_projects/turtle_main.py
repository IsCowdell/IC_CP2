import turtle 
from Helporturle import getMid,drawTriangle,sierpinski
def main():
   depth = input("what depth do you want(1-5) please:")
   depthnum = int(depth)
   t = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-100,-50],[0,100],[100,-50]]
   sierpinski(myPoints,depthnum,t,getMid,drawTriangle)
   myWin.exitonclick()

main()
