def utopianTree(n):
	initialHeight=1
	currentHeight=1
	if n==0:
		return 1
	else:
		for i in range(n+1):
			if i==0:
				pass
			else:
				if(not(i%2==0)):
					currentHeight*=2
				elif(i%2==0):
					currentHeight+=1
	return currentHeight

a=utopianTree(1)
print(a)