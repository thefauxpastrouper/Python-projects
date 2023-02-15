# Python Program to check whether the given input is alphabet, number or special character

#importing num2words
from num2words import num2words

ch = input("Please Enter Any Character : ")

if (ch.isalpha()): 
    print(f"The Given Character {ch} is an Alphabet")
    if (ch.isupper()):
        print(f"the given charater {ch} is in uppercase") 
    elif(ch.islower()):
        print(f"The Given Character {ch} is in lowercase")


elif (ch.isdigit()):
    print(f"The Given Character {ch} is a Digit")
    print(num2words(ch))

    
else:
    print(f"The Given Character {ch} is a Special Character")