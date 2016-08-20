OVERPASS_API         = overpy.Overpass()
BASE_DIR             = os.path.join(os.path.abspath('.'), 'work-flow')
URBAN_BOUNDARIES_FILE = '06_Europe_Cities_boundaries_with_Labels_Population.geo.json'

# Paths to base datasets that we are using:
URBAN_BOUNDARIES_PATH = os.path.join(BASE_DIR,URBAN_BOUNDARIES_FILE)
POIS_PATH            = os.path.join(BASE_DIR, "pois.json")

try:
    geo_df
except NameError:
    geo_df = GeoDataFrame.from_file(URBAN_BOUNDARIES_PATH)
    # Add a WKT column for use later
    geo_df['wkt'] = pandas.Series(
        map(lambda geom: str(geom.to_wkt()), geo_df['geometry']),
        index=geo_df.index, dtype='string')

try:
    boundaries_from_pd
except NameError:
    boundaries_from_pd = sqlContext.createDataFrame(geo_df)
    boundaries_from_pd.registerTempTable("boundaries")

try:
    pois_df
except NameError:
    pois_df = sqlContext.read.json(POIS_PATH)
    pois_df = pois_df.toPandas()
    def toWktColumn(coords):
        return (Point(coords).wkt)

    pois_df['wkt'] = pandas.Series(
        map(lambda geom: toWktColumn(geom.coordinates), pois_df['geometry']),
        index=pois_df.index, dtype='string')

    pois_df = sqlContext.createDataFrame(pois_df)
