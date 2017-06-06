# Description
This collection of scripts aids in the plotting of electric fields.
This is meant to be used as an educational tool.

# Usage

This is a basic example. We first create a "domain" where the fields
will act. Then we add the particles which create "electric fields".
Finally we have to bake the field to calculate the total field.

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

# Output
![](https://github.com/carlosb/fieldgraph/blob/master/Example/output.png)

# Requirements
- pylab
- numpy
- matplotlib
