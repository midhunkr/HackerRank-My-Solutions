def jumpingOnClouds(c, k):
	# c=an array of integers representing clouds
	# k=number of steps
	energyLevel=100
	stop=False
	start=True
	i=0
	while(not(stop)):
		if(start):
			i=(i+k)%len(c)
			start=False
		else:
			if(c[i]==0):
				energyLevel-=1
			elif(c[i]==1):
				energyLevel-=3
			if(i==0):
				stop=True
			else:
				i=(i+k)%len(c)

	return energyLevel

jumpingOnClouds([0,0,1,0],2)

		