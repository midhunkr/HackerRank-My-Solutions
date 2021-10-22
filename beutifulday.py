def rerverseNumber(i):
	reverse=0
	remainder=0
	while(i>0):
		remainder=i%10
		reverse=(reverse*10)+remainder
		i=i//10
	return reverse



def beautifulDays(i, j, k):
#i=starting day number
# j=ending day number12	
	reverse=0
	numberOfBeautifuldays=0
	for i in range(i,j+1):
		reverse=rerverseNumber(i)
		if(abs(reverse-i)%k==0):
			print(i)
			print("reverse is",reverse)
			
			numberOfBeautifuldays+=1
	return numberOfBeautifuldays


a=beautifulDays(49860,205494,155635764)
print(a)