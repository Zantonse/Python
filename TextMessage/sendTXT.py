import urllib
import tkinter as tk
from tkinter import *


class ButtonCall(Frame):

	def __init__(self, master=None):
		frame = Frame(master)
		frame.pack()
		def callback():
			sendmessage()
			
		self.button =  Button(frame, text="Turn Done", command = callback)
		self.button.pack()
		
#	def acceptButton():
#		
#		master = tk.Tk()
#		print ("callback")
#		
#		f = tk.Frame(master, height=32, width=32)
#		f.pack()
#		print ("framepack")
#		
#		B = tk.Button(master, text="Turn Done", command = callback, anchor="S")
#		f.pack_propogate(0) # don't shrink
#		B.pack(fill=BOTH, expand=1)
#		print ("button made")
#		mainloop()
		
		
	def sendMessage():

		number = 9014831164
		message = "Your Turn"
		carrier = 'AT&T'
		prov = ''
		url2 = 'http://www.txt2day.com/lookup.php'
		url = 'http://www.onlinetextmessage.com/send.php'
		if 'Verizon' in carrier:
			prov = '203'
		if 'AT&T' in carrier:
			prov = '41'
		values = {'number' : number,
				  'from' : 'craigv@ami.com',
				  'remember' : 'n',
				  'subject' : 'Welcome',
				  'carrier' : prov,
				  'quicktext' : '',
				  'message' : message,
				  's' : 'Send Message'}
		print ("send text now")
		data = urllib.urlencode(values)  ##text sender
		req = urllib.Request(url, data)
		response = urllib.urlopen(req)
		the_page = response.read() 
		
	
		
root = Tk()
app = ButtonCall(root)
root.mainloop()