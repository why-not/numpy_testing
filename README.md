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

```
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
```

## Test on AWS Ubuntu Image optimized for Deep Learning. (c5d.2xlarge: 8 cores, 16 GB Ram) 

```
ubuntu@ip-172-30-0-9:~$ source activate mxnet_p36
(mxnet_p36) ubuntu@ip-172-30-0-9:~$ ipython
Python 3.6.5 |Anaconda, Inc.| (default, Apr 29 2018, 16:14:56)
Type 'copyright', 'credits' or 'license' for more information
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: run test.py
generate_data, N times = 50 times: 0.04426059433999995 seconds per loop
sum axis=0 N times= 200 times: 0.009342705459999934 seconds per loop
sum axis=1 N times = 200 times: 0.013293346549999967 seconds per loop
sum full N times= 200 times: 0.013351381415000106 seconds per loop
mean 32 N times = 200 times: 0.009968762909999923 seconds per loop

In [2]: run test.py
generate_data, N times = 50 times: 0.04374865192000016 seconds per loop
sum axis=0 N times= 200 times: 0.009376861555000034 seconds per loop
sum axis=1 N times = 200 times: 0.012888064189999967 seconds per loop
sum full N times= 200 times: 0.012832252030000007 seconds per loop
mean 32 N times = 200 times: 0.009922239149999967 seconds per loop

In [3]: run test.py
generate_data, N times = 50 times: 0.04357514243999958 seconds per loop
sum axis=0 N times= 200 times: 0.009447478594999979 seconds per loop
sum axis=1 N times = 200 times: 0.013025719820000035 seconds per loop
sum full N times= 200 times: 0.013008963770000008 seconds per loop
mean 32 N times = 200 times: 0.009978990769999996 seconds per loop
```

## Test on AWS Ubuntu Image optimized for Deep Learning. (t2.nano: 1 cores, 0.5 GB Ram, Smallest Possible Amazon Server) 

```
In [1]: run test.py
generate_data, N times = 50 times: 0.06553657586 seconds per loop
sum axis=0 N times= 200 times: 0.013732203115000025 seconds per loop
sum axis=1 N times = 200 times: 0.016420330545000007 seconds per loop
sum full N times= 200 times: 0.01639490290000001 seconds per loop
mean 32 N times = 200 times: 0.015590667734999961 seconds per loop

In [2]: run test.py
generate_data, N times = 50 times: 0.06461507319999982 seconds per loop
sum axis=0 N times= 200 times: 0.01365810035999992 seconds per loop
sum axis=1 N times = 200 times: 0.016625747829999968 seconds per loop
sum full N times= 200 times: 0.01636717886999989 seconds per loop
mean 32 N times = 200 times: 0.0157351610149999 seconds per loop

In [3]: run test.py
generate_data, N times = 50 times: 0.06342938600000025 seconds per loop
sum axis=0 N times= 200 times: 0.013575194484999997 seconds per loop
sum axis=1 N times = 200 times: 0.01668353084000003 seconds per loop
sum full N times= 200 times: 0.016531246105000008 seconds per loop
mean 32 N times = 200 times: 0.015784036969999988 seconds per loop
```

## Information About Installed Linear Algebra Accelerators 

(Same for all the amazon tests) 

```
apt-cache policy liblapack3
liblapack3:
  Installed: 3.6.0-2ubuntu2
  Candidate: 3.6.0-2ubuntu2
  Version table:
 *** 3.6.0-2ubuntu2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu xenial/main amd64 Packages
        100 /var/lib/dpkg/status
(mxnet_p36) ubuntu@ip-172-30-0-9:~$ apt-cache policy libblas3
libblas3:
  Installed: 3.6.0-2ubuntu2
  Candidate: 3.6.0-2ubuntu2
  Version table:
 *** 3.6.0-2ubuntu2 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu xenial/main amd64 Packages
        100 /var/lib/dpkg/status
(mxnet_p36) ubuntu@ip-172-30-0-9:~$ apt-cache policy libatlas-base-dev
libatlas-base-dev:
  Installed: 3.10.2-9
  Candidate: 3.10.2-9
  Version table:
 *** 3.10.2-9 500
        500 http://us-east-1.ec2.archive.ubuntu.com/ubuntu xenial/universe amd64 Packages
        100 /var/lib/dpkg/status
```

## How to disengage LAPACK, BLAS, ATLAS on mac and linux

I have asked https://apple.stackexchange.com/questions/368380/lapack-blas-atlas-on-mac-book-pro-2017-mojave

references:
- [LAPACK] https://en.wikipedia.org/wiki/LAPACK
- [BLAS] http://www.netlib.org/blas/
- [ATLAS] https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software
