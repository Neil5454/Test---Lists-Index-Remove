import random

x = ['Jess','Jack','Mary','Sophia','Karen','Addison','Joseph','Eric','Ilona','Jason']

i = random.sample(range(len(x)), 2)
print(i[0])
print(i[1])
a = x[i[0]]
print(a)
b = x[i[1]]
print(b)
print(x)
x.remove(a)
x.remove(b)
print(x)