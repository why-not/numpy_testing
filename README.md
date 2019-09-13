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
## Mac Book Pro Hardware information
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


## How to disengage LAPACK, BLAS, ATLAS on mac and linux

I have asked https://apple.stackexchange.com/questions/368380/lapack-blas-atlas-on-mac-book-pro-2017-mojave

references:
- [LAPACK] https://en.wikipedia.org/wiki/LAPACK
- [BLAS] http://www.netlib.org/blas/
- [ATLAS] https://en.wikipedia.org/wiki/Automatically_Tuned_Linear_Algebra_Software
