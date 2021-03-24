def fib(number):
    if(number == 0):
        return 0
    elif(number == 1):
        return 1
    else:
        return (fib(number - 1) + fib(number - 2))

number = 0
for i in range(0,number):
    print(fib(i))

'''
Harjoitus 1
Kirjoita rekursiivinen funktio, joka tulostaa Fibonaccin lukujonon n ensimmäistä termiä.
Fibonaccin lukujono muodostuu seuraavasti:
F(n) = 0, kun n = 0
F(n) = 1, kun n = 1
F(n) = F(n-1) + F(n-2), kun n > 1
Lähde: https://fi.wikipedia.org/wiki/Fibonaccin_lukujono

Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.
'''
