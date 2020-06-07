str="abc123xyz"
for i in str:
	if i.isalpha():
		str=str.replace(i," ")
sum=0
for i in str.split():
	sum=sum+int(i)
print(sum)