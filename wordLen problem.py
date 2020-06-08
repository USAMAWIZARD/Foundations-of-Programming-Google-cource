arr=["a", "bb", "a", "bb"]
arr=list(set(arr))
dic=dict()
for i in arr:
	dic[i]=len(i)
print(dic)