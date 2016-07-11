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
    if total>m*n:
    	print("the die value is:",dice)
        print ("this die value is not acceptable")
        total=total-dice
    x=(total-1)%n
    y=(total-1)//n
    if y%2==1:
    	x=(n-1)-x
    print ("the position is", y,x)
if total==m*n:
    print ("you've won")
    print("the position is",y,x)
