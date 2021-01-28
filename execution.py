class parse:
	def __init__(self, executions):

		self.macro_running = True
		#print(executions, " received")

		while self.macro_running == True:
			for e in executions:
				self.execute(e)
			break

	def execute(self, e):
		print(e)