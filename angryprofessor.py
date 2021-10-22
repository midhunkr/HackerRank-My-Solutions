def angryProfessor(k, a):
	threshold_count=a
	ls=k
	current_count=0
	for i in ls:
		if i<=0:
			current_count+=1
	if current_count>=threshold_count:
		return 'YES'
	else:
		return 'NO'

k=[-2,0,1,2]
a=angryProfessor(k,3)
print(a)
