# Alkuperäisestä sanasta uusi sana, otetaan joka toinen kirjain.

word = 'mansikkamaa'
result = word[0]
for i in range(2, len(word), 2):
  result += word[i]

print(result)