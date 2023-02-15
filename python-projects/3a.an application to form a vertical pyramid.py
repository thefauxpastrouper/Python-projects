#Defining a function pyramid
def pyramid(height):
    for row in range(height):
        spaces = height - row + 5
        stars = 2 * row + 1
        print(" " * spaces + "*" * stars)

# taking the value of height from the user
height = int(input("enter no of rows: "))

# calling pyramid function
pyramid(height)
