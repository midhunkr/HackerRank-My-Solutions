def hurdleRace(k, height):
	maximuHeight=max(height)
	differ=0
	if(maximuHeight>k):
		differ=abs(maximuHeight-k)
	
	return differ

ls=[2,5,4,5,2]

a=hurdleRace(7,ls)
print(a)
