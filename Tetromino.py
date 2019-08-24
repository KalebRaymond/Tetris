class tS:
	state = [[['+' for _ in range(3)] for _ in range(3)] for _ in range(4)] #Four 3x3 matrices
	state_index = 0
	cur_state = state[state_index]
	
	def __init__(self):		
		self.state[0][1][0] = "█"
		self.state[0][1][1] = "█"
		self.state[0][0][1] = "█"
		self.state[0][0][2] = "█"
		
		self.state[1][0][1] = "█"
		self.state[1][1][1] = "█"
		self.state[1][1][2] = "█"
		self.state[1][2][2] = "█"
		
		self.state[2][2][0] = "█"
		self.state[2][1][1] = "█"
		self.state[2][2][1] = "█"
		self.state[2][1][2] = "█"
		
		self.state[3][0][0] = "█"
		self.state[3][1][0] = "█"
		self.state[3][1][1] = "█"
		self.state[3][2][1] = "█"
	
	def rotate(self):
		self.state_index = (self.state_index + 1) % 4 
		self.cur_state = self.state[self.state_index]
		
	def gprint(self):
		for row in self.cur_state:
			for e in row:
				print(e, end="")
			print(end="\n")
		
tetro = tS()

for i in range(5):
	tetro.gprint()
	tetro.rotate()
	print(end="\n")

	