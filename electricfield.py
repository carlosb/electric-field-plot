class ElectricField:
	"""
	This class describes an elecric field of a particle.
	""""

	def __init__(self, vx, vy, charge, pos):
		self.x = vx
		self.y = vy
		self.charge = charge
		self.pos = pos

		q = self.charge
		self.vx = q*(vx-pos[0])/((vx-pos[0])**2+(vy-pos[1])**2)**(.5)
		self.vy = q*(vy-pos[1])/((vx-pos[0])**2+(vy-pos[1])**2)**(.5)

	def getIntensity(self):
		return ((self.vx)**2 + (self.vy)**2)**(0.5)

	def add(self, E1):
		if (E1 == 0):
			pass
		self.vx += E1.vx
		self.vy += E1.vy
