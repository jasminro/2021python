'''
Harjoitus 1
Kirjoita funktio, joka ottaa parametrina määrittämättömän määrän numeroita ja 
kertoo ne yhteen. Funktio palauttaa tuloksen paluuarvona.
'''

def multiply(numbers) :     
    current = 0
    total = 0
    while numbers and len(numbers) > 0:
        total * numbers.pop()
        current += 1
    else:
        print(total) 

numbers = [1, 2, 3, 4]