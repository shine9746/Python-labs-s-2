a = input("Enter a string : ").casefold()
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
print ("Character frequency of the string ",a,"is - ",str(b))

