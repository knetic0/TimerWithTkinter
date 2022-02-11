import time
from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Kronometre')

root.grid_columnconfigure(2, weight=1)

minute = IntVar()
second = IntVar()


minute.set('00')
second.set('00')

def start(var):
	pass

Label(root, text='Kronometre',font=('Berlin Sans FB',18)).grid(column=2)

Label(root,text='Minute =',font=('Berlin Sans FB',16)).grid(column=1)

minEnt = Entry(root,textvariable=minute,width=10,font=('Berlin Sans FB',18))
minEnt.grid(column=1,row=1,columnspan=2)

Label(root,text='Second =',font=('Berlin Sans FB',16)).grid(column=1)
secEnt = Entry(root,textvariable=second,width=10,font=('Berlin Sans FB',18))
secEnt.grid(column=1,row=2,columnspan=2)

startButton = Button(root,text='Start',width=16,state=NORMAL,command=lambda :start(1))
startButton.grid(column=1,row=3,columnspan=2)


def start(var):

	if var == 1:
		startButton.config(state=DISABLED)
		timer = int(minute.get()) * 60 + int(second.get())
		i = 0
		global minTimer
		global secTimer

		isOver = Label(root,text='')
		isOver.grid(column=1,row=6,columnspan=2)

		minTimer = minute.get()
		secTimer = second.get()

		while i < timer:
			if secTimer != 0:
				secTimer -= 1
				time.sleep(1)
				minute.set(minTimer)
				second.set(secTimer)

				minEnt.config(textvariable=minute)
				secEnt.config(textvariable=second)

			elif secTimer == 0:
				minTimer -= 1
				secTimer = 59
				time.sleep(1)
				minute.set(minTimer)
				second.set(secTimer)

				minEnt.config(textvariable=minute)
				secEnt.config(textvariable=second)

			if secTimer == 0 and minTimer == 0:
				isOver.config(text='Time is Over!',font=('Berlin Sans FB',18))
				startButton.config(state=ACTIVE)
			i += 1
			root.update()
		time.sleep(3)
		isOver.config(text='')

root.mainloop()






















'''
mins = int(input('Dakikayi giriniz = '))
secs = int(input('Saniyeyi giriniz = '))

print('{} : {}'.format(mins,secs))

timer = mins*60 + secs

for i in range(0,timer):
	if secs != 0:
		secs -= 1
		time.sleep(1)
		print('{} : {}'.format(mins,secs))
	elif secs == 0:
		mins -= 1
		secs = 59
		time.sleep(1)
		print('{} : {}'.format(mins,secs))

print('Sure Doldu!')
'''