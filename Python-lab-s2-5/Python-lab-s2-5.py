dic1={1:10, 2:20}  #question
dic2={3:30, 4:40}
dic3={5:50,6:60}



a = dic1.items()    #converted to tuples
b = dic2.items()
c = dic3.items()

x = list(a)         #converted to list
y = list(b)
z = list(c)

d = x+y+z           #concatenated

e = dict(d)         #convert back to dict



print(type(e))
print(e)
