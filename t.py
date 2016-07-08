import random
sum=0
while sum<16:
    dice=random.randrange(1,7)
    print ("the die value is" ,dice)
    if(sum<16):
       sum=sum+ dice
       print(sum)
       x=sum%4
       y=sum//4

    if y%2==1:
       x=3-x
       
    print ("the position is", x,y)
    print("\n")
if sum==16:
     print ("you've won")
elif sum>16:
     print ("this die value is not acceptable")
     print (" the value of die is",dice)
	 
    

 

    
        
    
