from fpdf import FPDF
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
# number = input("enter a valid INR number")
# currency = input("enter a valid currency from the list")
number = os.getenv("number")
currency = os.getenv("input_currency")
print(currency)
print(number)
y = float(g[currency])
z = int(number) * y
# print(f"\n Currency conversion of INR {number} to {currency} is {z}  ")
output = f"\n Currency conversion of INR {number} to {currency} is {z}"

# save FPDF() class into a variable pdf
pdf = FPDF()
# Add a page
pdf.add_page()
# set style and size of font that you want in the pdf
pdf.set_font("Arial", size=15)
# create a cell
pdf.cell(200, 10, txt=output, ln=1, align='C')
# save the pdf with name .pdf
pdf.output("currency.pdf")
