
#modular arithematic
def saveThePrisoner(n, m, s):
	# n=no. of prisoners
	# m=no. of sweets
	# s=starting position
	# time limit exceeded for the below code
	
	# position=s-1
	# for i in range(m):
	# 	position=(position+1)%n
	# 	# print(position)

	# if position==0:
	# 		position=n
	# return position
	# print("the final pos",position)
	a=0
	a=(s+(m-1))%n
	if a==0:
		return n
	else:
		return a

a=saveThePrisoner(5,3,3)
print(a)

