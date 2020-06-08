from  tkinter import *
import csv
import random
wrong=5
def guesscheck():
	global textt,sentencetoguess,lb,wrong
	cor=0
	guess=textt.get("1.0","end-1c");

	rono=5
	for i in sentencetoguess.split(" "):
		col=0
		for spaceofaletter in i:
			if guess==spaceofaletter:
				lb=Label( text="  ______"+guess+"_______  " ).grid(row=rono,column=col)
				cor=1

			col+=1
		rono+=30
		rono+=30
		col=0


	if wrong<=0:
		pass
		
	elif wrong==5:
		print("""
		_______________
		|		|	
		|		|
		|		|
		|		|
		|		|	
		|______________|""")	

	elif wrong==4:
		pass
	elif wrong==3:
		pass
	elif wrong==2:
		pass
	
	elif wrong==1:
		pass

	wrong-=1
	
print("""------------------------------
			|
			|
			|
			|
			|"""
		)		
	


	
wordlist=[]
master = Tk()
master.geometry("800x800")
textt = Text(master,width=3,height=2)
textt.grid(row=0)

buttonCommit=Button(master, height=1, width=10, text="Guess",command=lambda: guesscheck()).grid(row=3)



file=open("wordlist.csv", "r")
reader = csv.reader(file)
for line in reader:
	wordlist=line


	
#seting gui for empty space
sentencetoguess=wordlist[random.randint(0,len(wordlist)-1)]
rono=5


for i in sentencetoguess.split(" "):
	lenghtofaword=len(list(i))

	col=0
	for spaceofaletter in range(lenghtofaword):
		lb=Label( text="  _____________  " ).grid(row=rono,column=col)
	
		col+=1
	rono+=30
	rono+=30
	col=0
e1 = Entry(master)
e1 = Entry(master)

mainloop()



