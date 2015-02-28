class ElectricField:
	"Class for the an electric field object"

	k0 = 8.99e9
	pi = 3.14159
	vx = 0
	vy = 0

	def __init__(self, vx, vy, charge=0, pos=[0,0]):
		self.charge = charge
		self.pos = pos
		self.vx, self.vy = computeComponents(vx,vy, pos)


	def getMagnitude(self, distance):
		if(self.distance > 0):
			return (self.charge/self.distance**2.)*self.k0
		else:
			return inf

	def computeComponents(self,x,y,a):
		return [q*(x-a[0])/((x-a[0])**2+(y-a[1])**2)**(.5),
			q*(y-a[1])/((x-a[0])**2+(y-a[1])**2)**(.5)]

	def add(self, E):
		return ElectricField(self.charge+E.charge, self.vx + E.vx, self.vy + E.vy)

