#IC decorator function

def decorator(func):
    def wrapper():
        print("before calling the function")
        func()
        print("after calling the function")
    return wrapper

@decorator
def greet():
    print("hello,world")

greet()
@decorator
def add():
    print(1+1)

add()