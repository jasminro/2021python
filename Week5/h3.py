def palindrome(word):
    word = word.lower()
    word = "".join(word.split())

    if len(word) <= 1: 
        return True
    elif word[0] != word[-1]: 
        return False
    return palindrome(word[1:-1])

strn = 'Saippuakauppias'
result = palindrome(strn)

if result==True:
    print("a palindrome!")
else:
    print("not a palindrome!")

'''
Harjoitus 3
Alla oleva funktio tarkistaa, onko sana palindromi. Kirjoita funktiosta rekursiivinen versio.
Ratkaisu voi olla helpompi, jos jaat sen useampaan funktioon.

def isPalindrome(word):
   word = word.lower()

   # Poistaa kaikki white spacet
   word = "".join(word.split())

   start = 0
   end = len(word) - 1

   while start <= end:
      if word[start] != word[end]:
         return False
      start += 1
      end -= 1
   return True
'''