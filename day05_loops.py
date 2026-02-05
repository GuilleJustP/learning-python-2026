"""
day05_loops.py
Learning FOR loops in Python
Author: Guillermo Justiniano Poehlmann
Date: 2026-01-23
"""
# Exercise 1: Print numbers from 1 to 5
from ast import While


for i in range(1,6):
    print(i)
# Exercise 2: Print numbers from 1 to 10
print("\n" + "="*40)
for i in range(1,11):
    print(i)
# Exercise 3: Sum of numbers from 1 to 10
total = 0
for i in range(1,11):
    total += i
print(f"\nLa suma de números del 1 al 10 es: {total}")
# Exercise 4: Loop through a list
paises = ["Brasil", "Indonesia", "USA", "China", "México"]

for pais in paises:
    print(f"\n Inmy career I want to visit {pais}")

# Exercise 5: Multiplication table of 7
total = 0
for i in range(1,12):
    total = 7 * i
    print(f"7 x {i} = {total}")

# Exercise 6: While loop
Count = 100
while Count < 110:
    print(Count)
    Count += 1   
Count = 0 
while Count <= 10:
    print(f"\n El valor actual de Count es: {Count} el cual es menor o igual a 10")
    Count += 2

# Exercise 7: Sum with While loop
total = 0
num = 1 
while num <= 100:
    total += num
    num *= 2
print(f"\n La suma de los números del 1 al 100 es: {total}")

# Exercise 8: Break while loop
num = 22
while True:
    if num %7 == 0:
        print(f"\n El número {num} es divisible por 7")
        break
    num += 1

# Exercise 9: Continue in for loop
num = 30
for i in range(1,40):
    if i % 2 == 0:
        continue
    print(f"\n Números impares entre 1 y 40: {i}")
    num += i

# Exercise 10: Triangle pattern

rows = 7
for i in range(4, rows + 1):
    print(" " * (rows - i) + "*" * i)

# Exercise 11: Multiplication table using nested loops

for i in range(1, 11):
    print (f"\n Tabla de multiplicar del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
       