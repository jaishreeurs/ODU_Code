import random
total=0
m=input("row:")
n=input("column:")
answer="yes"
z=[[0 for x in range(m)] for y in range(n)]
while answer=="yes":
	dice=random.randrange(1,7)
	if(total<m*n):
		total=total+ dice
	if total>m*n:
		total=total-(m*n)
	if total==m*n:
		total=0
	print("the die value is:",dice)
	print(total)
	x=(total-1)%n
	y=(total-1)//n
	if y%2==1:
		x=(n-1)-x
	print ("the position is", y,x)
	z[x][y]=1
	for x in range(m):
		for y in range(n):
			print(z[x][y])
		print('\n')
	rowtotal=[sum(z[x]) for x in range(m)]
	print("sum of row elements:",rowtotal)
	columntotal=[sum(z[y]) for y in range(n)]
	print("sum of column elements:",columntotal)
	if m in rowtotal:
		print("bingo!You won")
	elif n in columntotal:
		print("bingo!You won") 
	print("do you want to roll the dice?:")
	answer=raw_input()
    