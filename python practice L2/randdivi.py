import random

print(random.sample([i for i in range(0,1000) if i%5==0 and i%7==0],5))