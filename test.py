"""
numpy testing
"""
import os
import timeit
os.path.isdir('/Users/femto-13/All-Projects-on-femto/LaserLab/Software/numpy_testing/')
root = '/Users/femto-13/All-Projects-on-femto/LaserLab/Software/numpy_testing/'
folder = 'xray_images/'

lst = os.listdir(folder)
import sys
sys.path.append('/Users/femto-13/All-Projects-on-femto/APS/Instrumentation/Software/Lauecollect/')
from PIL import Image
from numpy import array

def import_images():
    from PIL import Image
    from numpy import array
    import os
    global folder
    lst = os.listdir(folder)
    data = []
    i = 0
    for item in lst:
        data.append(array(Image.open(folder+item)))
        i+=1
    return array(data)
data = import_images()

def sum_axis0():
    global data
    return data.sum(axis = 0)

def sum_axis1():
    global data
    return data.sum(axis = 1)

def sum_full():
    global data
    return data.sum()

def mean():
    global data
    return data.mean()

if __name__ is "__main__":
    N = 5
    res = timeit.timeit(stmt = import_images, setup = '', number = N)
    print("read 32 images N = {} times: {} seconds per loop".format(N,res/N))

    N = 20
    res = timeit.timeit(stmt = sum_axis0, setup = '', number = N)
    print("sum axis=0 32 images N = {} times: {} seconds per loop".format(N,res/N))

    N = 20
    res = timeit.timeit(stmt = sum_axis1, setup = '', number = N)
    print("sum axis=1 32 images N = {} times: {} seconds per loop".format(N,res/N))

    N = 20
    res = timeit.timeit(stmt = sum_full, setup = '', number = N)
    print("sum full 32 images N = {} times: {} seconds per loop".format(N,res/N))

    N = 20
    res = timeit.timeit(stmt = mean, setup = '', number = N)
    print("mean 32 images N = {} times: {} seconds per loop".format(N,res/N))
