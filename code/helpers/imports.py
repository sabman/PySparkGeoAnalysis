import notebook
import os.path, json, io, pandas
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['figure.figsize'] = (16, 20)

from retrying import retry # for exponential back down when calling TurboOverdrive API

import pyspark.sql.functions as func # resuse as func.coalace for example
from pyspark.sql.types import StringType, IntegerType, FloatType, DoubleType,DecimalType

import pandas as pandas
from geopandas import GeoDataFrame # Loading boundaries Data
from shapely.geometry import Point, Polygon, shape # creating geospatial data
from shapely import wkb, wkt # creating and parsing geospatial data
import overpy # OpenStreetMap API

from ast import literal_eval as make_tuple # used to decode data from java

# make sure nbextensions are installed
notebook.nbextensions.check_nbextension('usability/codefolding', user=True)

try:
    sc
except NameError:
    import pyspark
    sc = pyspark.SparkContext('local[*]')
    sqlContext = pyspark.sql.SQLContext(sc)
