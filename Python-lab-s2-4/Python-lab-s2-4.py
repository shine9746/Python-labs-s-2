#print count  of repeated characters

a = input("Enter a string : ").casefold()
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1

for i in b:
    if b[i] > 1:

        print(i,":",b[i])

