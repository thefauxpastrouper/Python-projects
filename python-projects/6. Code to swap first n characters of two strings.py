def swap(string_one, string_two):
	n= int(input("enter the no of first letters to remove: "))
	x = string_one[0:n] + string_two[n:]
	y = string_two[0:n] + string_one[n:]
	return x, y 
 
 
one, two = input("enter a word: "), input("enter another word: ")
print(one, two)  
 
print(swap(one, two)) 
