#!-*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox as mb
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack() 
        #pack()������Widget���뵽�������У���ʵ�ֲ��֡�
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel=Label(self,text='Hello,world!')
		self.helloLabel.pack()
		self.quitButton=Button(self,text='Quit',command=self.quit())
		self.quitButton.pack()
		'''self.nameInput=Entry(self)
		self.nameInput.pack()
		self.alterButton=Button(self,text='Hello',command=self.hello)
		self.alterButton.pack()'''
		
       #��createWidgets()�����У����Ǵ���һ��Label��һ��Button����Button�����ʱ������self.quit()ʹ�����˳���
	def hello(self):
		name=self.nameInput.get() or'world'
		mb.showinfo('Message','Hello,%s' %name)
app=Application()
app.master.title('Hello World!')
app.mainloop()
