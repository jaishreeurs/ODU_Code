import random
total=0
m=input("row:")
n=input("column:")
while total!=m*n:
    dice=random.randrange(1,7)
    print ("the die value is" ,dice)
    if(total<m*n):
        
        total=total+ dice
        print(total)
        x=total%n
        y=total//n
        if y%2==1:
            x=(n-1)-x
    print ("the position is", y,x)
    
         
    while total>m*n:
        print ("this die value is not acceptable")
        total=total-dice
        dice=random.randint(1,6)
        print("the die value is",dice)
        total=total+dice
        print(total)
        print ("the position is", y,x)
        print("\n")
if total==m*n:
    print ("you've won")
    print("the position is",y,x)
