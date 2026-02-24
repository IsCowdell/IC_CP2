#IC 1st 

for num in range(1,11):
    if num % 2 ==0:
        print(num)


even = []
num = 9
sum = 1 
for x in range(1,num+1):
    sum *= x 
print(f"loop:{sum}")

def factorial(n):
    if n == 1: return 1 #base case
    return n * factorial(n-1)
print(f"recursion:{factorial(num)}")
