#This file corresponds to the exercises result of the next tutorial
#https://www.tutorialspoint.com/python/python_control_flow.htm
#This tutorial contains the use of if, elif, else, match, case, break
# Loop for, for "in", range, for on dicts, 
#While, and else, break, continue, pass/... for loops

marks = 80
result = ""
if marks < 30:
    result = "Failed"
elif marks > 75:
    result = "Passed with distinction"
else:
    result = "Passed"

print(result)

def checkVowel(n): #More similar to switch from Rust or Haskell, only the first pattern that matches gets executed
    match n:
        case 'a' | 'e' | 'i'| 'o' | 'u': return "Vowel alphabet"
        case _: return "Other consonant"

def pruebaIdentacion():
 x=2
 print(x)

pruebaIdentacion()
print (checkVowel('u'))
print (checkVowel('f'))

'''
countries = ["Albania", "Armenia", "Azerbaiyan", "Uzbekistan"]
for country in countries:
    input("Do you like " + country + "? ")

mexicanStates = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila"]
states = len(mexicanStates)
while states > 0:
    print (mexicanStates[states-1])
    states-=1

discount, price = 0, 10001
if price>10000:
    discount = price*20/100
elif price>5000 & price<=10000:
    discount = price*10/100
elif price>1000 & price <=5000:
    discount = price*5/100
else:
    discount = 0
    
price -=discount
print ("You are going to pay " + str(price))

def greeting(details):
    match details:
        case [time, *names]:
            msg=''
            for name in names:
                msg+=f'Good {time} {name}!\n'
            return msg
        
print (greeting (["Nacht", "Lui"]))
print (greeting(["Tardes", "Abraham", "Juano", "Dixtinox"]))

def intr(details):
    match details:
        case [amt, duration] if amt<10000:
            return amt*10*duration/100
        case [amt, duration] if amt>=10000:
            return amt*15*duration/100
print ("Interest = ", intr([5000,5]))
print ("Interest = ", intr([15000,3]))
'''

#Loops      iterating_var in sequence
#           statements(s)                   (list, tuple or string)
greetingsEarthHabitants = "Hi there people from earth, are you doing human things?"
for char in greetingsEarthHabitants:
    if char not in 'aeiou':
        print (char, end='')
print ("\n")
numbers = range(5)
print (list(numbers))

for num in range(5):
    print (num, '*2=',(num*2), end=' ', sep='')
print("\n")

fact=1
N=5
for x in range(1, N+1):
    fact=fact*x
print("facotrial of {} is {}".format(N, fact))

numerotes = [34,54,67,21,78]
indices = range(len(numbers))
for index in indices:
    print ("index:", index, "number:", numerotes[index])

stats = {"health": 200, "speed": 100, "weight": 250, "stamina": 120}
for key, value in stats.items():  #We can access items, keys and values
    print (key, ":", value)

"""for stat in stats:           #Otra forma de hacerlo
    print(stat, ":", stats[stat])"""

#A for loop can contain an else statement
for count in range(6):
    print ("Iteration no. {}".format(count))
else:
    print ("for loop over. Now in else block")
print ("End of for loop")

for i in range(1,11): #Nested for loops
    for j in range(1,11):
        k=i*j
        print ("{:3d}".format(k), end=' ')
    print()

cuenta = 0
while cuenta < 5:
    cuenta+=1
    print(f"Iteration no. {cuenta}")
print("Endo of while loop")

paraWhileElse = 0
while paraWhileElse < 5 :
    paraWhileElse += 1
    print (f"Iteration no. {paraWhileElse}")
else:
    print (f"Whoops! Se acabó el while loop")
print ("End of while loop")

"""En python, los ciclos for y while pueden tener un statement
else, que se ejecuta en caso de que se terminen las iteraciones
del ciclo"""

for letter in 'Python':
    if letter == 'h':
        break
    print ('Current Letter: ', letter)

print ("\n")
for letter in 'Python':
    if letter == 'h':
        continue
    print ('Current Letter :', letter)

'''Los ciclos for y while también pueden usar break para
detener el flujo del ciclo, y continue para saltar a la
siguiente iteración del ciclo'''

n = int(input("\n Hola humano, dame un número"))
divisor = 2
while n>1:
    if n%divisor ==0:
        print (divisor)
        n = n/divisor
    else:
        divisor+=1

for letter in 'Python':
    if letter == 'h':
        pass #Pass statement does absolutly nothing :thumbs_up:
        ... #Python also allows using 3 dots called Ellipses as a pass statement
    print('Current letter: ', letter)