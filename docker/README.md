# A Small Course on Big Data - GeoAnalysis using PySpark

Clone the repository and use the provided `Dockerfile` to the buid image:

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
docker run -itd -p 8888:8888 sabman/geo-with-pyspark jupyter notebook '--ip=*'
```

OR

Enter and run the workshop environment from bash
```sh
docker run -it -p 8888:8888 sabman/geo-with-pyspark bash
jupyter notebook --ip=*
```

## Jupyter environment
Access Jupyter workshop environment via your browser
```sh
http://<docker ip>:8888
```
