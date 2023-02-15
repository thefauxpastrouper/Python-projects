str1 = input('Enter the string 1 :')
str2 = input('Enter the string 2 :')


res = [i for i in range(len(str1)) if str1.startswith(str2, i)]
ind=str(res)
l=[ind,len(str2)]

print("The start/ending indices of the substrings are : " ,l)
