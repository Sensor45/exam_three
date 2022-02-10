
import random

a = []
b = []

for i in range(10):
    a.append(random.randint(0, 20))
    b.append(random.randint(0, 20))

c = list(set(a) & set(b))

print(f'Элементы списка a - {a}')
print(f'Элементы списка b - {b}')
print(f'Cписок общих для а и b элементов - {c}')

