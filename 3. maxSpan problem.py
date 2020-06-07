import math
array=[1, 2, 1, 1, 3]
i=0
size=-math.inf
while i<len(array):
	j=i+1
	while j<len(array):
		if array[i]==array[j]:
			if (j-i) > size:
				size=j-i
		j+=1
	i+=1
print(size+1)