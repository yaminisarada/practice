from random import randint

throws = 0
num1 = 0

for n in range(1, 10):
    num = randint(1,6)
    if num >=1 or num<=6:
        throws+=1
        num1+=num
        print(throws,num,num1)
        
        
num2=num1/throws
num3=int(num2)

print("the number is: ", num3)
        
