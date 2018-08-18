from random import randint

heads=0
tails=0

for trial in range(0,100):
    while randint(0,1)==0:
        heads+=1
    tails+=1

print("heads/tails = ", heads/tails) 
