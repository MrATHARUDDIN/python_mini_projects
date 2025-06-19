# variable scope = where a variable is visiable and accessible
# scope resolution = (LEGB) local -> Enclosed -> GLobal -> Built-in

from math import e # Built in variable

b=2
def fun1():
    a=1
    print(a)

def fun2():
    print(b)

# here in fun1 "a" is local variable
# here in fun2 "b" is a Global variable


# scope resolution is a advance concept where 
# the permmion of using variable is goes in this order
# local -> Enclosed -> GLobal -> Built-in
x=3 # global
def fun3():
    x=1 # Enclose
    def fun4():
        x=2 # local
        print(x)
    fun4()
fun3()