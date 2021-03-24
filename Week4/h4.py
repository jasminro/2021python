'''
Harjoitus 4
Kirjoita funktio, joka laskee parametrina välitetyn positiivisen kokonaisluvun
kertoman. Toteuta myös virheiden käsittely.
Määritelmä: "Positiivisen kokonaisluvun n kertoma on luvun n ja kaikkien sitä pienempien 
positiivisten kokonaislukujen tulo, ja se merkitään n!."
(Wikipedia, https://fi.wikipedia.org/wiki/Kertoma)
 
Nollan kertomaksi on sovittu 1.
'''

n = int(input("Enter a positive number : "))
x = 1

for i in range(1,n+1): 
    x = x * i
      
print ("The factorial is : ",end="") 
print (x) 