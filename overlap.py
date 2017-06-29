import random
lista=random.sample(range(1,101), 30)
listb=random.sample(range(1,101),30)
listc=[a for a in lista if a in listb]
print("The comman elements in Both the list is {} ".listc)