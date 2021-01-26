try:

	import time
	import string
	import sys

	import tkinter as tk
	from tkinter import *
	
	import threading
	from threading import Thread
	
	from pynput.keyboard import Key, Controller, Listener
	from pynput.mouse import Button, Controller
	keyboard = Controller()
	mouse = Controller()

except:
	print("trouble installing packages")

class ui:
	def __init__(self):
		self.record_macrokey = "."
		self.execute_macrokey = ","
		self.main()

	def main(self):
		root = Tk()
		root.title("macro's")
		root.geometry("400x400")
		root.bind(self.record_macrokey, record)
		root.bind(self.execute_macrokey, execute)

		recordmacrobtn = tk.Button(root, width=20, height=2, text="Record Macro",  fg="white", bg="#263D42", command=record)
		recordmacrobtn.grid()

		executemacrobtn = tk.Button(root, width=20, height=2, text="Execute Macro",  fg="white", bg="#263D42", command=execute)
		executemacrobtn.grid()

		mainloop()

def record(event=""):
	print("record macro function ran")

def save():
	print("save macro function ran")
	
def execute(event=""):
	print("execute macro function ran")

def load(file):
	print("load macro function ran")

if __name__ == "__main__":
	ui()
