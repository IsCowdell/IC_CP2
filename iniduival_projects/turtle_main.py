import turtle 

from Helporturle import getMid,drawTriangle,sierpinski
#asking the depth of  triangle 
def main():
   depth = input("what depth do you want(1-5) please:")
   depthnum = int(depth)
     #need to make an if loop here chekcing th ecolor to print the triangle correctly
    #also asking the user what color they want 
   colors = ['yellow','blue','green','red','purple']
   colormap = input("What color do you want to choose from(yellow','blue','green','red','purple): ")
#once color is found not in it run it back
   if colormap not in colors:
      print("invaild color")
      return
   #making turtle look good
   t = turtle.Turtle()
   #postint the screen up 
   myWin = turtle.Screen()
   #setting poitns to start
   myPoints = [[-100,-50],[0,100],[100,-50]]
   #calling on function
   sierpinski(myPoints,depthnum,t)
   #exiting out of turtle 
   myWin.exitonclick()

main()
