import random
import sys
rowtotal=0
columntotal=0
total=0
m=input("row:")
n=input("column:")
answer="yes"
z=[[0 for x in range(m)] for y in range(n)]
def check():
    for x in range(m):
        for y in range(n):
            print(z[x][y])
        print('\n')
    rowtotal=[sum(z[x]) for x in range(m)]
    print("sum of row elements:",rowtotal)
    columntotal=[sum(x) for x in zip(*z)]
    print("sum of column elements:",columntotal)
    if m in rowtotal:
        print("bingo!You won")
        sys.exit()
    elif n in columntotal:
        print("bingo!You won") 
        sys.exit()
def position(): 
    y=(total-1)%n
    x=(total-1)//n
    if x%2==1:
        y=(n-1)-y
    print ("the position is", x,y)
    z[x][y]=1
    check()
while 'true':
    dice=random.randrange(1,7)
    if(total<m*n):
        total=total+ dice
    if total>m*n:
        total=total-(m*n)
    if total==m*n:
        total=0
    print("the die value is:",dice)
    print(total)
    position()

    
    