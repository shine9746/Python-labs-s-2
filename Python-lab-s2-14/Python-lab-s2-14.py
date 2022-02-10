#Python programme to remove an item from a set if it is present in the set
a = {"apple","banana","cherry","dates","orange","grape","plum","lemon"}

print("The orginal set : ",a)


try:
   b=input("Enter the item to be removed : ")

   a.remove(b)

   print("Ans:",a)

   print(b.capitalize(),"removed from the orginal set")

except:
    print("Please enter a valid item!!!")


