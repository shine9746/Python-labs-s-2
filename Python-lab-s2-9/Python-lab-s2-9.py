#python programme to find the index of a tuple


a = ("apple","mango","grape","pineapple","banana","pomegranate","jackfruit","cherry","plum","strawberry","lemon")

print(a)

b = input("enter a tuple element : ")

try:
    print("The index of tuple element ",b,"is",a.index(b))
except:
    print("Please enter a valid tuple element!!!")
