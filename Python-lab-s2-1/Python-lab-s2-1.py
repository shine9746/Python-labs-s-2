#shows all possible strings of a,e,i,o,u , using the characters exactlty once

import random
x = ["a","e","i","o","u"]

random.shuffle(x)
print("".join(x))

