'''
Harjoitus 3
Kirjoita funktio, joka laskee parametrina saadun sanan vokaalisen määrän. Vokaaleja
ovat kirjaimet [a, e, i, o, u, y, ä, ö] (ts. suomen kielen mukaiset vokaalit :)
'''

'''
str1 = input("Enter your word: ")
vowels = 0
 
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y' or i == 'ä' or i == 'ö'):
        vowels = vowels + 1
 
print("There are this many vowels in the word = ", vowels)
'''

def vowels(word):
    word = word.lower()
    vowels = ("a", "e", "i", "o", "u", "y", "ä", "ö")
    result = 0
    for char in word:
        if char in vowels:
            result += 1
    return result
