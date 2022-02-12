#python programme for password generator,mix of alphabets(lowercase/uppercase),numbers,symbols

import random
import string


characters = string.printable[:-6] #printable executes alphabets,digits,symbols

charactersToList = list(characters) #to list

lengthOfPassword = int(input("Enter the length of password : "))  #inputs length of password

lengthOfList = len(charactersToList)  #length of list

random.shuffle(charactersToList)  #shuffled list

for i in range(0,lengthOfList-lengthOfPassword):        #iterated and croped unwanted length
    charactersToList.pop()


print("Your random password is : ",''.join(charactersToList)) 