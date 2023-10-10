text='python is aprogramming language'
vowel=("a","e","i","o","u")
words=text.split(" ")
for w in words:
    if w.casefold().startswith('i'):
        print(w)