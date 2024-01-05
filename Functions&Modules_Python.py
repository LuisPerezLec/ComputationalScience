#Python, unlike c/c++, uses pass by reference mechanism
#for arguments on function calling

# Anyway, inside or outside a function, if you try to change
# an inmutable object (like an int), it won't modify the value
# but it will create a new object with the new value, this also applies
# for inmutable objects sent as arguments to functions.
#
# With mutable objects, it won't happen, for example, if
# we sent a dict as an argument, and we modify it inside the
# function, its id will remain the same, and its value will
# be also changed on the global representation of the dict.

#Docstrings -> Documentation strings
#First string statement on a function, util for defining
#the function objective, it can help to generate automatic
#documentation and guide about the objective and way of use
#of the function.
#It also can be accessed with the __doc__ atribute or
#the help() function
#
#help(id) <- Accessing to the docstring of a built-in function

def testfunction(arg):
    print ("ID inside the function:", id(arg))
    #You can ommit the return statement by reducing the
    #indent after last statement, but using explicit
    #return is a good practice :thumbs_up:

var="Hello"
print ("ID inside the function: ", id(var))
testfunction(var)

# Types of Functions
# -Built-in functions -> int() len() sum()
# -Functions in built-in modules *Needs to be imported
# -User-defined functions

def greetings( str ):
    "This is docstring of greetings function"
    print ( str)
    return

greetings("Hello, fellow humans")

def testfunctionDict(arg):
   print ("Inside function:",arg)
   print ("ID inside the function:", id(arg))
   arg=arg.append(100)
   
varDict=[10, 20, 30, 40]
print ("ID before passing:", id(varDict))
testfunctionDict(varDict)
print ("list after function call", varDict)

#def function1(arg1, arg2):  #Here arg1 and arg2 are called Formal arguments
#   ...
#   ...
#   return
#
# function1(val1, val2)     #Here val1 and val2 are called Actual arguments

#Types of arguments:
#Positional or required arguments
#Keyword arguments
#Default arguments
#Positional-only arguments
#Keyword-only arguments
#Arbitrary or variable-length arguments
#
# def function (a, b, /, c, d, e=v1, f=v2, *arg, *, g, h, i=v3, **kwarg)
# Where a,b are positional-only, c,d are regular positional
# e and f are default args, *arg is arbitrary positional
# g,h,i are keyword only and **kwarg is arbitrary kw args

#You can call a function by positional arguments:
#printinfo ("Luis", 21)
#or by keyword arguments
#printinfo (name = "Lui", age = 21)

#https://www.tutorialspoint.com/python/python_keyword_arguments.htm
