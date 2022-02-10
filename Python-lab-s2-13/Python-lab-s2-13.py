#generate all sublists of a list
a = ["a","b","c","d"]

b = []

for i in range(len(a) + 1):

    for x in range(i + 1, len(a) + 1):
        b.append(a[i:x])

print("Orginal list is",a)

print("Sublists of a are : ")
print(b)