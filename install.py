from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
name = 'SampleApp' # Program name
defpath = '/path/to/folder/' # Path where program would be installed (not required)
zippath = 'SampleApp.zip' # An zip of your program and files which program needs
def setpath():
	global defpath
	defpath = path.get()
	setuplabel.config(text=f'You are about to install {name} to {defpath} is this correct?')
	steps.select(2)
def install():
	import os
	if not os.path.exists(defpath):
		os.makedirs(defpath)
	import zipfile
	with zipfile.ZipFile(zippath, 'r') as zip:
		zip.extractall(defpath)
	messagebox.showinfo('Info','Installing done!')
	root.destroy()
root.title(name + ' Installer')
imgbanner = PhotoImage(file='banner.png')
imagebanner=ttk.Label(image=imgbanner)
imagebanner.pack(side=LEFT,expand=True,fill=Y)
steps = ttk.Notebook(root)
tab1 = ttk.Frame(steps)
tab2 = ttk.Frame(steps)
tab3 = ttk.Frame(steps)
label1=ttk.Label(tab1,text="Welcome to installation wizard\nYou are about to install "+name)
label1.grid(row=0, column=0)
startbutton=ttk.Button(tab1,text='Install',command=lambda: steps.select(1))
label2=ttk.Label(tab2,text=f'Enter location of where {name} would be')
path = ttk.Entry(tab2)
installbtn = ttk.Button(tab2,text='Next',command=lambda: setpath())
label2.pack()
path.pack()
installbtn.pack()
setuplabel=Label(tab3,text=f'You are about to install {name} to {defpath} is this correct?')
setuplabel.pack()
realinstallbtn = Button(tab3,text='Yes & install',command=install)
realinstallbtn.pack()
startbutton.grid(row=1,column=0,pady=100)
steps.add(tab1, text ='Start')
steps.add(tab2, text ='Location')
steps.add(tab3, text ='Installation')
steps.pack(side=TOP)
root.mainloop()