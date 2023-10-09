'''
Tristan Deveyra
2057603
'''


word = str(input())
nospace_word = word.replace(" ", "")
new = nospace_word[::-1]

if nospace_word == new:
  print(word, "is a palindrome")
else:
  print(word, "is not a palindrome")
