import os
file = 'currency.txt'
a = open(file)
b = a.readlines()
g = {}
for c in b:
    d = c.split("\t")
    e = d[1]
    f = d[0]
    g[f] = e
print('give from the list of available currencies:\n')
[print(h) for h in g.keys()]
number = os.getenv("number")
currency = os.getenv("input_currency")
print(currency)
print(number)
y = float(g[currency])
z = int(number) * y
print(f"\n Currency conversion of INR {number} to {currency} is {z}  ")
