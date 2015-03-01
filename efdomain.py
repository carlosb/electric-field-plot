from pylab import plot, plt, streamplot, quiver, xlabel, ylabel, axis, show, close
from numpy import linspace, meshgrid
import electricfield as ef

class Domain:

	fields = []

	# xlabel('$x$')
	# ylabel('$y$')
	# axis('image')

	def __init__(self, x=[-1,1], y=[-1,1], x_indexing=16, y_indexing=16):
		# create linear spaces
		self.x = linspace(x[0], x[1], x_indexing)
		self.y = linspace(y[0], y[1], y_indexing)

		# generate xy grid
		self.x, self.y = meshgrid(self.x, self.y)

		self.total_field = ef.ElectricField(self.x, self.y, 0, [(x[0]+x[1])/2,(y[0]+y[1])/2])
	

	def add_field(self, charge, pos):
		self.fields.append(ef.ElectricField(self.x,self.y,charge, pos))

	def bake(self):
		self.total_field = ef.ElectricField(self.x, self.y, 0, [0,0])
		for E in self.fields:
			self.total_field.add(E)


	def plot(self, type='plot'):
		close('all')
		E = self.total_field
		if(type == 'plot'):
			plot(E.vx, E.vy)
			show()
		elif(type == 'streamplot'):
			streamplot(self.x,self.y,E.vx,E.vy, density=2,color=E.getIntensity(), linewidth=2, cmap=plt.cm.hot)
			show()
		elif(type == 'quiver'):
			quiver(self.x, self.y, E.vx, E.vy, pivot='middle', headwidth=4, headlength=6)
			show()