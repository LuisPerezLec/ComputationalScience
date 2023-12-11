#raw_input("\n\nPress the enter key to exit")
import sys;
x = "foo"; print(id(x)) #Con id imprimimos la ubicacion en memoria
del x #Esto esto borra la variable x
a=b=c=10 #3 variables con el mismo valor
del a,b,c
a,b,c = 10,20,30 #3 variables con diferente valor

'''En c/c++, al declarar una variable int a=10, estamos asignando
el valor de 10 al espacio en memoria de a, en cambio, en python,
al escribir a=10, estamos haciendo una referencia al objeto 10, y
si más de una variable tiene el mismo valor, estas variables están
referenciando al mismo objeto
'''

variable1, variable2 = 10, '10'
if variable1==variable2: #Compara la referencia del objeto al que apuntan
    print("Esto no se imprime")
else:
    print("Esto sí se imprime") #Porque apuntan a diferentes objetos

# Data types
# Numeric: int, float, complex; String:str
# Sequence: list, tuple, range; Binary: bytes, bytearray, memoryview
# Mapping: dict; Boolean: Bool
# Set: set, frozenset; None: NoneType

print("El tipo de variable 1:", type(variable1), "\nEl tipo de variable 2:", type(variable2))

""" str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string """

""" list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists """

# Tuples are read-only lists, their values cant't be updated

#range(start, stop, step)   - All integers

#Dictionary keys should be immutable objects, and cann't appear more than once in a collection
#if a key is saved twice, the last one will remain
dict = {} #Dictionary is not a sequence, but it is mutable, you can add, modify and delete
dict['one'] = "Value for the first key"
dict[2] = "Value for the second key"

tinydict = {'name': 'john', 'code':6734, 'dept': 'sales'}
print(tinydict)

# The set is a mutable hashed structure
#The positions of items in the set are optimized to perform operations
#A set can store only immutable objects
#An object cann't appear more than once in a set.
arrangedSet = {2023, "Python", 3.11, 5+6j, 1.23E-4}
print(arrangedSet)

## Conversion / Casting
#Python, unlike js (which is weakly typed), is strongly typed
#this doesn't allow automatic type conversion between unrelated
#data types.

# Integer = 4 bytes of memory
# Float = 8 bytes of memory

#Implicit casting
# python doesn't automatically convert float -> int to avoid data lossing
# On the other hand, python can easily int -> float
intNum = 10; floatNum = 10.5; implicitConversion = intNum + floatNum
print("Conversión implícita", implicitConversion)
#We can also implicitly conver boolean up to float, where true = 1
print(10.5+True) #10.5 + True = 11.5

#Explicit casting
## int() function
intCasting1 = int(2*3.14)
intCasting2 = int(True)
intCasting3 = int("100")
#It can cast from binary, octal and hexa-decimal adding a parameter
intCasting4 = int("110011", 2) #51
incCasting5 = int("2A9", 16) #681

## float() function
floatCasting1 = float(100) #100.0
floatCasting2 = float("1234.5") #Without comas
floatCasting3 = float("1.00E-4") #0.0001

## str() function
strCasting1 = str(True) #'True'
strCasting2 = str(11.10) #'11.1'
strCasting3 = str(2/5) #'0.4'

#List, tuple and string are ordered or indexed collection of items
listCasting = list("Hello") #['H','e','l','l','o']
tupleCasting = tuple("Hello") #('H','e','l','l','o')
strCasting4 = str([1,2,3,4,5]) #'[1, 2, 3, 4, 5]'

# Podemos convertir a int, long, float, complex, str, repr
# eval, tuple, list, set, dict, frozenset, chr, unichr, ord
# hex, oct

var = "3/4"
print(var)
var = "\u00BE"
print(var)

# Python's unicode support
toencode = "Hello"
onbytes = toencode.encode('utf-8') #Encoding string
print(onbytes)
todecode = onbytes.decode('utf-8') #Decoding byte object back to str
print(todecode)

toencode = "\u20B9"
print("\n\n", toencode)
onbytes = toencode.encode('utf-8') #Encoding Rupee symbol
print(onbytes)
todecode = onbytes.decode('utf-8')
print(todecode)

#Python literal's ¿
print("\n\n")
octal = 0O34
print("0O34 in octal is", octal, type(octal))
hexa = 0X1c
print("0X1c in Hexadecimal is",hexa, type(hexa))

#Default delimiter for Python sequence is parentheses, so if you
#don't add anything on a comma separated sequence it becomes a tuple
T1=1,"Ravi",75.50, True
print (T1, type(T1))


#Operators
## Arithmetic, Comparison, Assignment, Logical
## Bitwise, Membership, Identity

#Arithmetic + - * / % ** //
#Comparison == != < <= => >
#Assignment = += -= *= /= %= **= //= &= |= ^= >>= <<=
#Bitwise & | ^ ~ << >>
#Logical and or not
#Membership     in      not in
#Identity       is      is not

##Operators precedence
# () [] {}
# [index] [index:index]
# await x
# **
# ~x +x -x
# * @ / % //
# + -
# >> <<
# &
# ^ |
# <= < > >=
# <> == !=
# = %= /= //= -= += *= **=
# is is not
# in not in
# not or and
# if - else
# lambda
# :=

# Logical operators

logicalOperator1, logicalOperator2 = 5, 10
if logicalOperator1 <10 and logicalOperator2 >5:
    print("Hola mundo")

print ("not (x+y>15):", not (logicalOperator1+logicalOperator2)>15)

# The expression  "x and y" first evaluates "x". If "x" is false, its value is returned, otherwhise "y" is evaluated and is returned
print(10 and 30) #30
print(30 and 10) #10
print(0 and 40) #0
print(50 and 0) #0

# The expresion "x or y" first evaluates "x". If "x" is true, its value is returned, otherwise "y" is evaluated and returned
print(10 or 30) #10
print(30 or 10) #30
print(0 or 40) #40
print(50 or 0) #50

# Bitwise operators
bitwise1, bitwise2 = 60, 13
print("a: ",a, "b:",b, "a&b:", a&b) #12

# 0011 1100
# &
# 0000 1101
# ---------
# 0000 1100  -> 12

# ^ -> XOR
print(~10)
print(~-10)
#00001010 10 a negativo complemento -1
#11110101 -> -11

#11110110 -> -10
#00001001 -> 9

import sys
print(sys.maxsize) #Max size for int (64bits or 8bytes)

#Left shift operator
#a: 60 a<<2: 240
#0011 1100
#<<2
#1111 0000

#Right shift operator
#a:60 a>>2:15
#0011 1100
#>>2
#0000 1111

print("a:7", 7>>2) #1

#Me quedé en
#https://www.tutorialspoint.com/python/python_membership_operators.htm