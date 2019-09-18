# Numpy Testing

the purpose of this repository is to learn more about LAPACK, BLAS and ATLAS.

## How to find the location of LAPACK, BLAS, ATLAS
one can use locate command (https://openmx.ssri.psu.edu/wiki/blas-library-help)

``locate libblas.so`` 

another way to get information about lapack, blas, atlas.  liblapack3, libblas3 , libatlas-base-dev(https://stackoverflow.com/questions/15851831/how-to-check-if-blas-and-atlas-already-installed)

```
apt-cache policy liblapack3
apt-cache policy libblas3
apt-cache policy libatlas-base-dev
```

currently I don't have them installed
```
(base) femtoland@femtoland:~$ apt-cache policy liblapack3
liblapack3:
  Installed: (none)
  Candidate: 3.7.1-4ubuntu1
  Version table:
     3.7.1-4ubuntu1 500
        500 http://us.archive.ubuntu.com/ubuntu bionic/main amd64 Packages
(base) femtoland@femtoland:~$ apt-cache policy libblas3
libblas3:
  Installed: (none)
  Candidate: 3.7.1-4ubuntu1
  Version table:
     3.7.1-4ubuntu1 500
        500 http://us.archive.ubuntu.com/ubuntu bionic/main amd64 Packages
(base) femtoland@femtoland:~$ apt-cache policy libatlas-base-dev
libatlas-base-dev:
  Installed: (none)
  Candidate: 3.10.3-5
  Version table:
     3.10.3-5 500
        500 http://us.archive.ubuntu.com/ubuntu bionic/universe amd64 Packages
```
## Test on Mac Book Pro
### Hardware information
  ```
  Model Name:	MacBook Pro
  Model Identifier:	MacBookPro14,1
  Processor Name:	Intel Core i5
  Processor Speed:	2.3 GHz
  Number of Processors:	1
  Total Number of Cores:	2
  L2 Cache (per Core):	256 KB
  L3 Cache:	4 MB
  Hyper-Threading Technology:	Enabled
  Memory:	16 GB
  Boot ROM Version:	198.0.0.0.0
  SMC Version (system):	2.43f6
  ```
### Results of tests
```
n [33]: run test.py
read 32 images 1 times: 2.53048706055 seconds per loop
sum axis=0 32 images 10 times: 0.612431001663 seconds per loop
sum axis=1 32 images 10 times: 0.39970459938 seconds per loop
sum full 32 images 10 times: 0.343644690514 seconds per loop
mean 32 images 10 times: 0.324725699425 seconds per loop

In [34]: run test.py
read 32 images N = 5 times: 3.28182039261 seconds per loop
sum axis=0 32 images N = 20 times: 0.698462152481 seconds per loop
sum axis=1 32 images N = 20 times: 0.39868710041 seconds per loop
sum full 32 images N = 20 times: 0.343178701401 seconds per loop
mean 32 images N = 20 times: 0.333559799194 seconds per loop

In [1]: run test.py
read 32 images N = 5 times: 2.56678800583 seconds per loop
sum axis=0 32 images N = 20 times: 0.611644756794 seconds per loop
sum axis=1 32 images N = 20 times: 0.397477507591 seconds per loop
sum full 32 images N = 20 times: 0.341990947723 seconds per loop
mean 32 images N = 20 times: 0.320617651939 seconds per loop
```


## Test on AWS Ubuntu Image optimized for Deep Learning. (t3a.2xlarge: 8 cores, 32 GB Ram) 

run test.py
generate_data, N times = 50 times: 0.05521430158000044 seconds per loop
sum axis=0 N times= 200 times: 0.013160574044999863 seconds per loop
sum axis=1 N times = 200 times: 0.013259274245000086 seconds per loop
sum full N times= 200 times: 0.01330458675000017 seconds per loop
mean 32 N times = 200 times: 0.01342332953500005 seconds per loop

run test.py 
generate_data, N times = 50 times: 0.05374531482000066 seconds per loop
sum axis=0 N times= 200 times: 0.011327756174999877 seconds per loop
sum axis=1 N times = 200 times: 0.013209703784999647 seconds per loop
sum full N times= 200 times: 0.013074761825000109 seconds per loop
mean 32 N times = 200 times: 0.013217427714999985 seconds per loop

run test.py 
generate_data, N times = 50 times: 0.05423383809999905 seconds per loop
sum axis=0 N times= 200 times: 0.011368431889999897 seconds per loop
sum axis=1 N times = 200 times: 0.013211888019999946 seconds per loop
sum full N times= 200 times: 0.013100763045000009 seconds per loop
mean 32 N times = 200 times: 0.013218856825000102 seconds per loop


## Test on AWS Ubuntu Image optimized for Deep Learning. (t3a.2xlarge: 8 cores, 32 GB Ram) 


## How to disengage LAPACK, BLAS, ATLAS on mac and linux

I have asked https://apple.stackexchange.com/questions/368380/lapack-blas-atlas-on-mac-book-pro-2017-mojave

references:
- [LAPACK] https://en.wikipedia.org/wiki/LAPACK
- [BLAS] http://www.netlib.org/blas/
- [ATLAS] https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software
