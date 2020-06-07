ballance=[2, 1, 1, 2, 1]
newball=ballance.copy()
right=[]
left=[]
target=sum(ballance)/2
canball=False
for i in ballance:
	if i<=target:
		tsum=i
		right.append(i)
	else:
		continue
		
	for j in ballance:
		if tsum+j<=target:
			tsum=tsum+j
			right.append(j)
		
		if sum(right) == target:

			ballance=newball.copy()
			for elem in right:
				ballance.remove(elem)

			left=ballance
			if sum(left)==sum(right):
				print("right",right,end="        ")
				print("left",left)
				canball=True
			ballance=newball.copy()
			tsum=i
			right=[tsum]

	right=[]
	left=[]
	
	
	
if canball:
	print("can balanced")
else:
	print("cannot ballance")