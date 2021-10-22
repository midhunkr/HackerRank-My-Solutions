def findDigits(n):
	digit=0
	count=0
	number=n
	while(not(n==0)):
		digit=n%10
		if(digit==0):
			pass
		else:
			if(number%digit==0):
				print("Value of digits",digit)
				count+=1
		n=n//10
	return count
	# print(count)

findDigits(123456789)

