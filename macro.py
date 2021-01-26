try:

	import time
	import string
	import sys

	import tkinter as tk
	from tkinter import *
	
	import threading
	from threading import Thread

	import mouse
	import keyboard

except:
	print("trouble installing packages")

class ui:
	def __init__(self):
		self.record_macrokey = "x"
		self.stoprecord_macrokey = "."
		self.execute_macrokey = "z"
		self.stopexecute_macrokey = ","
		self.eventlist = []
		self.executelist = []
		self.main()

	def main(self):
		root = Tk()
		root.title("macro's")
		root.geometry("400x400")
		root.bind(self.record())
		root.bind(self.execute())

		recordmacrobtn = tk.Button(root, width=20, height=2, text="Record Macro",  fg="white", bg="#263D42", command=self.record)
		recordmacrobtn.grid()

		executemacrobtn = tk.Button(root, width=20, height=2, text="Load Macro",  fg="white", bg="#263D42", command=self.load)
		executemacrobtn.grid()

		executemacrobtn = tk.Button(root, width=20, height=2, text="Execute Macro",  fg="white", bg="#263D42", command=self.execute)
		executemacrobtn.grid()

		mainloop()

	def record(self, event=""):

		print("record macro function ran")

		# log mouse/keyboard action

		filename = "test.txt"
		self.save(filename)


	def save(self, filename):
		print("save macro function ran")

		# test inputs
		self.eventlist = ["g","a","y"]

		# write input to txt
		file = open(filename, "w")
		for line in self.eventlist:
			file.write(line + "\n")

	def load(self, file=""):
		print("load macro function ran")

		from tkinter.filedialog import askopenfile
		file = askopenfile(mode="r")
		if file is not None:
			content = file.read()
			for instruction in content:
				self.executelist.append(instruction)

	def execute(self, event=""):
		print("execute macro function ran")
		# handle instructions in self.executelist

	
if __name__ == "__main__":
	ui()
