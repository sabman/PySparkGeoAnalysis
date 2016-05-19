# A Small Course on Big Data - GeoAnalysis using PySpark

Download the `Dockerfile` to the buid image. Then proceed as below:

## Docker build
Build the docker image
```sh
docker build -t sabman/pydata-berlin-2016-geo-with-pyspark .
```

## Docker run

Run the workshop environment directly
```sh
docker run -it -p 8888:8888 sabman/pydata-berlin-2016-geo-with-pyspark
```

OR

Enter and run the workshop environment from bash
```sh
docker run -it -p 8888:8888 sabman/pydata-berlin-2016-geo-with-pyspark bash
jupyter notebook --ip=*
```

## Jupyter environment
Access Jupyter workshop environment via your browser
```sh
http://<docker ip>:8888
```
