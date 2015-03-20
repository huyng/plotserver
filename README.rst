webplot
=======

Expose your matplotlib figures over http with 1 line of code


Installation
------------

.. code-block:: shell

    pip install webplot


Example usage
-------------


plotting a pylab environment

.. code-block:: python

    import webplot as wpl
    import pylab
    pylab.plot([1,2,3,4,1,2,3,4])
    pylab.xlabel("numbers")
    pylab.ylabel("values")

    # display plot using webserver at http://0.0.0.0:8080/
    wpl.show(pylab)


plotting a matplotlib figure

.. code-block:: python

    import webplot as wpl
    from matplotlib import pyplot

    fig = pyplot.figure()
    axes = fig.gca()
    axes.plot([1,2,3,4,1,2,3,4])

    # display plot using webserver at http://127.0.0.1:9999/
    wpl.show(fig, host="127.0.0.1", port=9999)

