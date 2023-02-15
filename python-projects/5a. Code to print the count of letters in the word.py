A = str(input("enter a word: "))

x = {}

for i in A:
    if i in x:
        x[i] += 1
    else:
        x[i] = 1

print(f"The count of all characters in the word: \n  {str(x)}")

