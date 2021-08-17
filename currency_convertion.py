import os
file = 'currency.txt'
a = open(file)
b= a.readlines()
#print(b)
g = {}
for c in b:
    #print(c.split("\t"))
    d = c.split("\t")
    e = d[1]
    f = d[0]
    g[f] = e
    #print(f)
    #print(e)
#print(g)
print('give from the list of available currencies:\n')
[print(h) for h in g.keys()]
# currency = input("\n enter a currency:")
# number = int(input("\n enter the INR amount: "))
number = os.getenv("number")
currency = os.getenv("input_currency")
print(currency)
print(number)
#currency = {currency}
#number = {number}
y = float(g[currency])
z = number * y
# print(f"\n Currency conversion of INR {number} to {currency} is {z}  ")
