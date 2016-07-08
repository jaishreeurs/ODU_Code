import random
total=0

while total!=16:
    dice=random.randrange(1,7)
    print ("the die value is" ,dice)
    if(total<16):
        rollAgain="yes"
        total=total+ dice
        print(total)
        x=(total-1)%4
        y=(total-1)//4
        if y%2==1:
            x=3-x
    print ("the position is", y,x)
    
         
    while total>16:
        print ("this die value is not acceptable")
        total=total-dice
        dice=random.randint(1,6)
        print("the die value is",dice)
        total=total+dice
        print(total)
        print ("the position is", y,x)
        print("\n")
if total==16:
    print ("you've won")
    

 

    
        
    
