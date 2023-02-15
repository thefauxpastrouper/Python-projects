#defining num
num = int(input("enter value: "))

#creating a for inside an if loop
if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print(f"{num} is not a prime number" )
          
        else:
            print(f"{num} is a prime number")
        break    
else:
    print(f"{num} is not a prime number")            
