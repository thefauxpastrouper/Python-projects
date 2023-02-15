#defining a function prime_numbers
def prime_numbers(n):
    for num in range(2, n + 1):
        prime = True
        for i in range(2, num):
            if (num % i) == 0:
                prime = False
                break
        if prime:
            print(num)

#taking an integer input 
n = int(input("Enter a number: "))

#calling the fuction prime_numbers
prime_numbers(n)