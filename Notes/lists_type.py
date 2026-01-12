#Ic 1st types of list notes

siblings = ["anai","cowdell","chris","jerel","jake","anai"]

print(siblings[3])

siblings[-2] = "feet"

print(siblings)


#tuples
fruit = ("apples","orange","peach","kiwi","raspberry",)
#not changable
home = (0,0)

x,y = home
#fruit[3] = "grape"
print(x)
#sets
colors = {"blue","yellow","pink","purple"}
colors.add("green")
colors.remove("green")
#no duplicates
print(colors)

for i in colors:
    if i == "pink":
        print("yoes")
    print(i)
