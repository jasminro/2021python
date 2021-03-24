'''
Harjoitus 5
Palindromi
Kirjoita funktio, joka tarkistaa, onko sana palindromi. Palindromi on sana, joka on sama
kirjoitettuna oikein ja väärin päin. Sanan kirjainten koolla ei ole merkitystä.
Oletus: Sana ei sisällä white space -merkkejä (rivinvaihto, välilyönti, tabulaattori).
Bonus: Sana saa sisältää white space -merkkejä, mutta niitä ei oteta huomioon tarkistettaessa,
onko sana palindromi.
'''

def isPalindrome(s):
    return s == s[::-1]
 
# Driver code
s = input("give a word : ")
ans = isPalindrome(s)
 
if ans:
    print("Yeah, it's a palindrome!")
else:
    print("Nope, it's not a palindrome.")