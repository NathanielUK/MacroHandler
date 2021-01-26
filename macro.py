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
		self.main()

	def main(self):
		root = Tk()
		root.title("macro's")
		root.geometry("400x400")

		recordmacrobtn = tk.Button(root, width=20, height=2, text="Record Macro",  fg="white", bg="#263D42", command=record_macro())
		recordmacrobtn.grid()

		executemacrobtn = tk.Button(root, width=20, height=2, text="Execute Macro",  fg="white", bg="#263D42", command=record_macro())
		executemacrobtn.grid()

		mainloop()

def record_macro():
	print("record macro function ran")

def save_macro():
	print("save macro function ran")
	
def execute_macro():
	print("execute macro function ran")

def load_macro(file):
	print("load macro function ran")

if __name__ == "__main__":
	ui()
