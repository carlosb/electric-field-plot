import efdomain as ed

D = ed.Domain([-5, 5], [-5,5])
D.add_field(10, [-2,0])
D.add_field(-7, [2,0])
D.bake()

D.plot('quiver')