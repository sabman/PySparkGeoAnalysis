# A Small Course on Big Data - GeoAnalysis using PySpark


## Option 1 :star: :star: :star: :star:

1. Get the Docker image from hard disk provided.

2. run the following:

```sh
docker load -i docker-image-geo-pyspark.tar

# expected output:
# bd33956a6f4f: Loading layer [==================================================>] 2.048 kB/2.048 kB
# 3dd3d8b12447: Loading layer [==================================================>]   255 MB/255 MB
# 92c3a0251fb4: Loading layer [==================================================>] 35.84 kB/35.84 kB
# 9d12afe8a154: Loading layer [==================================================>] 2.106 MB/2.106 MB
# c31e7d394c7a: Loading layer [==================================================>]  42.5 kB/42.5 kB
# 58488c0819b0: Loading layer [==================================================>] 153.4 MB/153.4 MB
# 6754bddd1d00: Loading layer [==================================================>] 526.8 kB/526.8 kB
# 6d74733a707d: Loading layer [==================================================>] 159.7 kB/159.7 kB
# da22252361f9: Loading layer [==================================================>] 291.8 kB/291.8 kB
# cdf772898f4e: Loading layer [==================================================>] 9.973 MB/9.973 MB
# 2f888cc370ad: Loading layer [==================================================>] 773.2 MB/773.2 MB
# bc54f62fb8a1: Loading layer [==================================================>] 578.3 MB/578.3 MB
# bcab5f1c62a3: Loading layer [==================================================>]   512 kB/512 kB
# e655e60c8c2a: Loading layer [==================================================>] 798.2 kB/798.2 kB
# 1251f472746b: Loading layer [==================================================>] 31.43 MB/31.43 MB
# d392bfe90dc4: Loading layer [==================================================>] 283.1 kB/283.1 kB
# 340caea9c2ac: Loading layer [==================================================>] 1.974 MB/1.974 MB


docker run -it -p 8888:8888 -p 4040:4040 sabman/geo-with-pyspark bash
jupyter notebook --ip=*
```

### Get you IP
```sh
docker-machine ip
# e.g. output
# 192.168.99.100
```

### Open PySpark notebook in browser

go to `http://<your-ip>:8888/tree`



## Option 2 :star: :star: :star:

Only if the internet is working very very well!

1. Pull Image from Docker Hub **WARNING don't do this if the network is slow**

```sh
docker pull sabman/geo-with-pyspark
docker run -it -p 8888:8888 -p 4040:4040 sabman/geo-with-pyspark bash
jupyter notebook --ip=*
```

----

# Development

## Building docker image from scratch

**DO NOT DO THIS - its for Development**

Clone the repository and use the provided `Dockerfile` to the build image:

```
git clone git@github.com:sabman/PySparkGeoAnalysis.git
```

Then proceed as below:

## Docker build
Build the docker image
```sh
docker build -t sabman/geo-with-pyspark -f ./docker/Dockerfile .
```

## Docker run

Run the workshop environment directly
```sh
docker run -itd -p 8888:8888 -p 4040:4040 sabman/geo-with-pyspark jupyter notebook '--ip=*'
```

OR

Enter and run the workshop environment from bash
```sh
docker run -it -p 8888:8888 -p 4040:4040 sabman/geo-with-pyspark bash
jupyter notebook --ip=*
```

## Jupyter environment
Access Jupyter workshop environment via your browser
```sh
http://<docker ip>:8888
```


4040
