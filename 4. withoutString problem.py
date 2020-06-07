string="hello there"
remove="e"
i=0
while  i <(len(string)+1):
	
	if remove==string[i:i+len(remove)]:
		string= string[0:i]+string[i+len(remove):]
	i+=1
	print(i)
print(string)	