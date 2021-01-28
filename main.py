try:

	import time
	import string
	import sys
	import os

	import tkinter as tk
	from tkinter import *
	
	from pynput import mouse, keyboard

except:
	print("trouble installing packages")

class ui:
	def __init__(self):
		self.record_macrokey = "x"
		self.macrostop = "."
		self.execute_macrokey = "z"
		self.executestop = ","
		self.running = False
		self.eventlist = []
		self.executelist = []
		self.foldername = "scripts"
		self.loadedmacro = ""
		self.main()

	def main(self):

		root = Tk()
		root.title("macro's")
		root.geometry("400x400")

		root.bind(self.record_macrokey, self.record)
		root.bind(self.macrostop, self.stoprecording)
		root.bind(self.execute_macrokey, self.execute)

		recordmacrobtn = tk.Button(root, width=20, height=2, text="Record Macro",  fg="white", bg="#263D42", command=self.record)
		recordmacrobtn.grid()

		loadmacrobtn = tk.Button(root, width=20, height=2, text="Load Macro",  fg="white", bg="#263D42", command=self.load)
		loadmacrobtn.grid()

		executemacrobtn = tk.Button(root, width=20, height=2, text="Execute Macro",  fg="white", bg="#263D42", command=self.execute)
		executemacrobtn.grid()

		global macrolbl
		macrolbl = tk.Label(root, width=20, height=2, text="",  fg="white", bg="#263D42")
		macrolbl.grid()

		root.mainloop()

	def stoprecording(self, event=""):
		self.running = False

	def record(self, event=""):

		print("record macro function ran")

		# log mouse/keyboard action

		def on_press(key):

			if self.running:

				msg = ("{}/down:{}".format(key, time.time()))
				#msg = msg.replace("'","")
				print(msg)
				self.eventlist.append([msg])

				# in a catch method because it crashes when ? pressed

				try:
					if key != key.space and key.char == self.macrostop:
						print("stop macro")
						listener.stop()
						filename = "test.txt"
						self.save(filename)
				except:

					try:
						if key.char == self.macrostop:
							print("stop macro")
							listener.stop()
							filename = "test.txt"
							self.save(filename)
					except:
						pass
		

		def on_release(key):

			if self.running:

				msg = ("{}/up:{}".format(key, time.time()))
				#msg = msg.replace("'","")
				print(msg)
				self.eventlist.append([msg])


		# start recording inputs

		if self.running == True:
			return
		elif self.running == False:
			listener = keyboard.Listener(
				on_press=on_press,
				on_release=on_release)
			listener.start()
			self.running = True


	def save(self, filename):
		print("save macro function ran")

		# test inputs
		# self.eventlist = ["g","a","y"]
		self.eventlist.remove(self.eventlist[-1])

		if os.path.isdir(self.foldername):
			pass
		else:
			os.mkdir(self.foldername)

		# write input to txt
		findpath = self.foldername+"\\"+filename
		file = open(findpath, "w")
		for line in self.eventlist:
			file.write(str(line) + "\n")
		file.close()

		self.eventlist = []
		self.running = False

	def load(self, file=""):
		print("load macro function ran")

		from tkinter.filedialog import askopenfile
		file = askopenfile(mode="r")
		self.loadedmacro = os.path.basename(file.name)
		print(self.loadedmacro)
		if file is not None:
			content = file.read()
			for instruction in content:
				self.executelist.append(instruction)
		else:
			print("no file found")
		global macrolbl
		macrolbl["text"] = self.loadedmacro


	def execute(self, event=""):
		print("execute macro function ran")
		from execution import parse
		# handle instructions in self.executelist
		print(self.executelist, " sent")
		parse(self.executelist)
		self.executelist = []

	
if __name__ == "__main__":
	ui()
	
