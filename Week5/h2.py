count = 0
def counting(number):
    global count
    if(number > 0):
        count = count + 1
        counting(number//10)
    return count

number = 234675432
count = counting(number)
print("Number of digits:", count)

'''
Harjoitus 2
Kirjoita funktio, joka laskee numeroiden määrän luvussa rekursiivisesti.
Esim. luvun 10253 tulos on 5 ja luvun 42 tulos on 2.
'''