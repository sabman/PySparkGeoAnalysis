# A Small Course on Big Data - GeoAnalysis using PySpark

## Option 1 :star: :star: :star: :star:

1. Get the Docker image from hard disk provided. (Ask Shoaib Burq) This is 6 Gigabyte.

2. Run the following command to load the docker image:

```sh
docker load -i docker-image-geo-pyspark.tar

# expected output:
# 3dd3d8b12447: Loading layer [==================================================>]   255 MB/255 MB
# 58488c0819b0: Loading layer [==================================================>] 153.4 MB/153.4 MB
# 6754bddd1d00: Loading layer [==================================================>] 526.8 kB/526.8 kB
# 6d74733a707d: Loading layer [==================================================>] 159.7 kB/159.7 kB
# da22252361f9: Loading layer [==================================================>] 291.8 kB/291.8 kB
# ...
# cdf772898f4e: Loading layer [==================================================>] 9.973 MB/9.973 MB
# 2f888cc370ad: Loading layer [==================================================>] 773.2 MB/773.2 MB
# bc54f62fb8a1: Loading layer [==================================================>] 578.3 MB/578.3 MB
# e655e60c8c2a: Loading layer [==================================================>] 798.2 kB/798.2 kB
# d392bfe90dc4: Loading layer [==================================================>] 283.1 kB/283.1 kB
# 340caea9c2ac: Loading layer [==================================================>] 1.974 MB/1.974 MB


docker run -it -p 8888:8888 -p 4040:4040 sabman/geo-with-pyspark bash
jupyter notebook --ip=*
```

**Get you IP**

```sh
docker-machine ip
# e.g. output
# 192.168.99.100
```

**Open PySpark notebook in browser**

go to `http://<your-ip>:8888/tree`


## Option 2 :star: :star: :star:

Only if the internet is working really really well!

1. Pull Image from Docker Hub **WARNING don't do this if the network is slow**

```sh
docker pull sabman/geo-with-pyspark
docker run -it -p 8888:8888 -p 4040:4040 sabman/geo-with-pyspark bash
jupyter notebook --ip=*
```

----

# Development

## Building docker image from scratch

**DO NOT DO THIS - its for Development purposes**

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
Access Spark Jupyter workshop environment via your browser:

```sh
http://<docker ip>:8888
```
