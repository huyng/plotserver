# webplotlib
Expose matplotlib figures over http


Example usage (plotting a pylab environment):

```
import webplotlib as wpl
import pylab
pylab.plot([1,2,3,4,1,2,3,4])
pylab.xlabel("numbers")
pylab.ylabel("values")

# display plot using webserver at http://localhost:8080/
wpl.show(pylab)
```

Example usage (plotting a matplotlib figure):


```
import webplotlib as wpl
from matplotlib import pyplot

fig = pyplot.figure()
axes = fig.gca()
axes.plot([1,2,3,4,1,2,3,4])

# display plot using webserver at http://localhost:8080/
wpl.show(fig)
```
