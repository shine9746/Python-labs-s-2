#shows all possible strings of a,e,i,o,u 

import random
x = ["a","e","i","o","u"]

random.shuffle(x)
print("".join(x))

