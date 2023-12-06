x = int(input("Pleas give me a numbe, please")) #Leer datos
if x < 0: #condicional
    x = 0
    print("Now it's zero")
elif x==0:
    print("It was already zero, bonk")
elif x==1:
    print('One, nice!')
else:
    print("I haven't meet that number yet")

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

pets = ["dark", "molly", "zuko", "blue"] #arreglo
for pet in pets: #for -> similar a un for each
    print(pet, "es mi mascota")

#Collection
users = {'Kaleb': 'activo', 'Emmanuel': 'inactivo', 'Hector': 'activo'}

for user, status in users.copy().items():
    if status == 'inactive':
        print('Se eliminara a', user)
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        print('Se agregó al usuario', user)
        active_users[user] = status

for i in range(5):
    print(i)

print('Lista de amigotes')
amigotes = ['Kaleb', 'Rot', 'Silvon', 'Calala', 'Roger']
for i in range(len(amigotes)):
    print((i+1), amigotes[i])

#For
for n in range(2, 3):
    print(n, 'Esto solo se imprimirá una vez')

#Numeros primos
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#Numeros pares e impares
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)

#El match funciona como un switch
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
        
print(http_error(404))
y = 25
print(f"Y={y}")

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
print(fib(39088168))