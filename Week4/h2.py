'''
Harjoitus 2
Kirjoita funktio, joka palauttaa suurimman luvun, mikä on tallennettu parametrina
saatuun tietorakenteeseen. Mieti myös sopiva arvo palautettavaksi siinä tapauksessa, että 
tietorakenne ei sisällä mitään lukuja.
Toteuta myös vastaava funktio, mikä palauttaa pienimmän luvun tietorakenteessa.
'''
NumList = []
Number = int(input("Enter the total of your numbers : "))
for i in range(1, Number + 1):
    value = int(input("Enter the value of number %d : " %i))
    NumList.append(value)

NumList.sort()

print("The largest element in this list is : ", NumList[Number - 1])
print("The smallest element in this list is : ", NumList[0])
