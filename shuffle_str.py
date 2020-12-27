import random

name = "sainath"

try:
 random.shuffle(name)
 print(name)
 
except TypeError:  # str is not used support for shuffling
    pass
 
finally:
     result = "".join(random.sample(name, len(name)))
     print(result)



