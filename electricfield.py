from pylab import plot, plt, streamplot, quiver, xlabel, ylabel, axis, show

class ElectricField:
	"Class for the an electric field object"
		
	xlabel('$x$')
	ylabel('$y$')
	axis('image')

	def __init__(self, vx, vy, charge=0, pos=[0,0]):

		
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
		self.vx += E1.vx
		self.vy += E1.vy

	def plot(self, type='plot'):
		if(type == 'plot'):
			plot(self.vx, self.vy)
			show()
		elif(type == 'streamplot'):
			streamplot(self.x,self.y,self.vx,self.vy, density=2,color=self.getIntensity(), linewidth=2, cmap=plt.cm.hot)
			show()
		elif(type == 'quiver'):
			quiver(self.x, self.y, self.vx, self.vy, pivot='middle', headwidth=4, headlength=6)
			show()