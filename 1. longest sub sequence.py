import math
str="abppplee"
wordlist=["able","ale","apple","bale","kangaroo"]
max=-math.inf

for i in wordlist:
	ind=0
	x=0
	size=0
	while ind<len(str) and x<len(str)-1:
		if str[x]==i[ind]:
			size+=1
			ind+=1
		if size==len(i)-1:
			if len(i)>max:
				long=i
				break
		x+=1
print(long)
	
	
	
