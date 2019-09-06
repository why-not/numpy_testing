"""
numpy testing
"""

class Test(object):
    def __init__(self):
        pass
    
    def generate_data(self):
        """
        generate 32 image, size = 3960x3960, values = random numbers, dtype= uint16.
        """
        from numpy import array, random
        lst = range(32)

        i = 0
        self.data = random.randint(2**16-1, size=(3960, 3960),dtype = 'uint16')


    def test_sum_axis0(self):
        return self.data.sum(axis = 0)

    def test_sum_axis1(self):
        return self.data.sum(axis = 1)

    def test_sum_full(self):
        return self.data.sum()

    def test_mean(self):
        return self.data.mean()

if __name__ == "__main__":
    import timeit
    test = Test()
    test.generate_data()
    N = 50
    res = timeit.timeit(stmt = test.generate_data, setup = '', number = N)
    print("generate_data, N times = {} times: {} seconds per loop".format(N,res/N))

    N = 200
    res = timeit.timeit(stmt = test.test_sum_axis0, setup = '', number = N)
    print("sum axis=0 N times= {} times: {} seconds per loop".format(N,res/N))

    N = 200
    res = timeit.timeit(stmt = test.test_sum_axis1, setup = '', number = N)
    print("sum axis=1 N times = {} times: {} seconds per loop".format(N,res/N))

    N = 200
    res = timeit.timeit(stmt = test.test_sum_full, setup = '', number = N)
    print("sum full N times= {} times: {} seconds per loop".format(N,res/N))

    N = 200
    res = timeit.timeit(stmt = test.test_mean, setup = '', number = N)
    print("mean 32 N times = {} times: {} seconds per loop".format(N,res/N))
