# fieldgraph
Graph electric fields....FOR NOW


# Usage

Goes something like this
```python
import efdomain as ed

# Domain(x_interval, y_interval, x_index=16, y_index=16)
D = ed.Domain([-5, 5], [-5,5])

# add_field(charge, position)
D.add_field(10, [-2,0])
D.add_field(-7, [2,0])

# computes the total field
D.bake()

# plot('plot_type')
# choose between 'plot', 'streamplot' and 'quiver'
D.plot('quiver')
```
This will output:
![](https://github.com/carlosb/fieldgraph/blob/master/Example/output.png)
