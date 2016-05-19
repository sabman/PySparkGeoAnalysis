# GEO optimized pyspark container
# This environment was build for a workshop demonstration on PyData Berlin 2016

FROM jupyter/pyspark-notebook

USER root

# Here are some informations how-to change the 'conda' environment
# https://hub.docker.com/r/pdonorio/py3dataconda/~/dockerfile

# Force bash always 
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Setup python 2.7 as default environment
ENV CONDA_ENV_PATH /opt/conda/envs/python2
ENV CONDA_DEFAULT_ENV python2
ENV CONDA_DIR /opt/conda
ENV CONDA_ACTIVATE "source $CONDA_ENV_PATH/bin/activate python2"
ENV PATH $CONDA_ENV_PATH/bin:$PATH

RUN apt-get update && apt-get install -y \
    curl \
    git-core \
    build-essential \
    cpio \
    python-pip \
    libpython-dev \
    libgeos-dev \
    libproj-dev \
    libgdal-dev \
    libspatialite-dev \
    && apt-get clean

# Install / upgrade python libs
RUN $CONDA_ACTIVATE && pip install overpy --upgrade
RUN $CONDA_ACTIVATE && pip install retrying --upgrade
RUN $CONDA_ACTIVATE && pip install geopandas --upgrade

# Install conda packages
RUN conda install libgfortran -y
RUN conda install fiona -y
RUN conda install gdal -y

# Get custom GEO libs
RUN curl -k -o /usr/local/lib/spatial-spark_2.10-1.1.1-beta-SNAPSHOT.jar https://dl.dropboxusercontent.com/u/96303065/spark-workshop/spatial-spark_2.10-1.1.1-beta-SNAPSHOT.jar \
    curl -o /usr/local/lib/jts-1.13.jar http://central.maven.org/maven2/com/vividsolutions/jts/1.13/jts-1.13.jar

# Add GEO libs to spark class path
ENV SPARK_CLASSPATH="/usr/local/lib/jts-1.13.jar:/usr/local/lib/spatial-spark_2.10-1.1.1-beta-SNAPSHOT.jar"

# Download the latest notebook and GEO data 
RUN mkdir -p /home/jovyan/work/work-flow \
    && curl -o /home/jovyan/work/work-flow/06_Europe_Cities_Boundries_with_Labels_Population.geo.json http://datax.academy/pydata-berlin-2016/06_Europe_Cities_Boundries_with_Labels_Population.geo.json \
    && curl -o /home/jovyan/work/work-flow/pois.json http://datax.academy/pydata-berlin-2016/pois.json \
    && curl -k -o /home/jovyan/work/Analysis.ipynb https://raw.githubusercontent.com/sabman/GeoAnalysis-of-Culture-in-European-Cities-Using-PySpark/master/Analysis.ipynb