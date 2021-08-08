
#Exercise 1
retained = 100
interest = 0.15
result = 100 * (1 + 0.15)**10
print(result)
#Exercise 2
x, y, z = 5, "Nimbus Python", True
var1 = var2 = var3 = 10
print(y + " 2020")
print(x/var1)
print((x+6)%var2)

x = "C++"
print("Hoc " + x)
def global_var():
    global x
    x = "Python"
    print("Hoc " + x)
global_var()
print("Hoc " + x)

a = 237
b = 829.17
c = 3 + 5j
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(isinstance(a, complex))
n = 19
m =complex(n + 1j)
print(m, n)
g = float(a)
print(g)

import random 

x,y,z = 1,2.8,3+7j
print(type(x))
print(type(y))
print(type(z))
complex(x)
print(x)

print(random.randrange(1,100))
print(random.randrange(1,100,3))

print(random.random())

print(random.uniform(-100.0, 100.0))

print(random.choice([1,2,3,5,8,13,21,34,55]))

print(random.choices([2,5,6,7,28,18,291,92]))

print(random.sample([3,4,5,6,7,8,9,10], k = 3))
