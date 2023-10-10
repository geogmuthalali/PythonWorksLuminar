#sequence of characters
name="geo g "
print(name.casefold()) #convert to lowercase
print(name.capitalize())# convert to uppercase
print(name.count('a'))# character occured
print(name.index('o')) #position of the character first occurance
print(name.strip('g')) #remove the particular character given either from the left or right not midddle
print(name.rstrip('g')) #remove from the right particular character
print(name.lstrip('g')) #remove from the left
print(name.isalpha()) #check whether the given string contain numeric numbers
print(name.isdigit()) #check digit or not
print(name.isalnum()) #exclude special  characters
#startwith #whether it starts the given character
#endswith # whether it ends the given charcter
#sort #soting in the alphabetic order
name="python is a programming language "
word=name.strip("")
for w in word:
    print(w)

    