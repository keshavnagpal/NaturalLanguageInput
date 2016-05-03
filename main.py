import speech_recognition as sr

#DemoData
c=['q','z','x','c','v','b','n','d','e','r']
p=[2,3,2,5,8,5,9,7,3,4]
m=[1,8,6,3,2,4,7,2,4,6]

#supported actions
actions=['show']
states=['high','low']
objects=['priority','maturity']
nested=['which','from','how']

#temporary list and full list
tlist=[]
flist=[0,1,2,3,4,5,6,7,8,9]

#action
def show(li,st,ob):
	global tlist
	tlist=[]
	if(st==states[0]):
		if(ob==objects[0]):
			for i in li:
				if(p[i]>5):
					print(c[i])
					tlist.append(i)
		if(ob==objects[1]):
			for i in li:
				if(m[i]>5):
					print(c[i])
					tlist.append(i)

	if(st==states[1]):
		if(ob==objects[0]):
			for i in li:
				if(p[i]<6):
					print(c[i])
					tlist.append(i)
		if(ob==objects[1]):
			for i in li:
				if(m[i]<6):
					print(c[i])
					tlist.append(i)

	#print(tlist)



#MainLoop
while(1):
	state=''
	obj=''
	ch=''
	#text input
	#ch=input("speak(i mean write for now) , write exit to exit\n")

	#speech input
	r=sr.Recognizer()
	with sr.Microphone() as source:
		print("speak")
		audio=r.listen(source)
	try:
		ch=r.recognize_google(audio)
	except sr.UnknownValueError:
		print("Google speech recognition could not understand this audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
		print("check your internet connection")
	try:
		if(ch=='exit'):
			exit()

		#making a list of words spoken/written
		chl=ch.split()

		#if the action is new
		l=flist
	
		#to check if the action is nested
		for i in range(3):
			if(chl[i] in nested):
				l=tlist

		for x in chl:
			if(x in states):
				state=x
			if(x in objects):
				obj=x

		show(l,state,obj)
	except:
		print("didn't recognize that")
