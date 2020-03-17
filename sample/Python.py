import numpy.matlib
from numpy.testing import assert_array_equal, assert_

def test_empty():
    x = numpy.matlib.empty((2,))
    assert_(isinstance(x, np.matrix))
    assert_(x.shape, (1, 2))

def test_ones():
    assert_array_equal(numpy.matlib.ones((2, 3)),
                       np.matrix([[ 1.,  1.,  1.],
                                 [ 1.,  1.,  1.]]))

    assert_array_equal(numpy.matlib.ones(2), np.matrix([[ 1.,  1.]]))

class MyClass():
    def __init__(self, message):
        self.value = message

myinstance = MyClass("Hello!")
print(myinstance.value)
