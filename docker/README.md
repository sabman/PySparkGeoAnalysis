# A Small Course on Big Data - GeoAnalysis using PySpark

## Docker build

Build the docker image

```sh
docker build -t sabman/pydata-berlin-2016-geo-with-pyspark .

## Docker run

Run workshop environment directly

```sh
docker run -it -p 8888:8888 sabman/pydata-berlin-2016-geo-with-pyspark

Enter and run the workshop environment from bash

```sh
docker run -it -p 8888:8888 sabman/pydata-berlin-2016-geo-with-pyspark bash
jupyter notebook -ip=*

## Jupyter environment

Acess Jupyter workshop environment via your browser
```sh
http://<docker ip>:8888
