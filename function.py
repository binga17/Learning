#global keyword for function

x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x)
myfunc()
print("Python is " + x)

#global variable inside a function use global keyword

def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)

#to change global variable inside the function used global keyword

x = "awesome"
def func():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)
