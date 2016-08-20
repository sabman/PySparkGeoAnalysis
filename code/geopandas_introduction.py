# Workflow
# Base data:
#   * City boundaries as GeoJSON
#   * POIs as GeoJSON
#
# Analysis:
#   For each City:
#       Intersect POIs with the City boundaries
#           Data quality issues with POIs not being within boundaries
#           Add a check for counting the number of cities
#           Clean POIs
#       Count the cultural sites
#       Divide by population
#       Output


# Below script collects the POIs of cultural significance for Bounding Boxes
# of all the cities and stores them in a GeoJSON file.

# We use the overpass-turbo.eu API to download the cultural data and it can
# only handle Bounding Boxes and not more detailed/exact boundaries.

from geopandas import GeoDataFrame
import os.path, overpy, json, io

# This function converts shapely bounds to Overpass bbox
# http://wiki.openstreetmap.org/wiki/Overpass_turbo/Extended_Overpass_Queries
# params bounds tuple: (minx, miny, maxx, maxy)
# return bbox tuple:   (miny, minx, maxy, maxx)
def bbox(bounds):
    return (bounds[1],bounds[0],bounds[3],bounds[2])

# This function converts a OpenStreetMap node into a GeoJSON Feature
def nodeToFeature(node):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                float(node.lon),
                float(node.lat)
            ]
        },
        "properties": node.tags
    }

# This function converts a collection of OpenStreetMap nodes into an array of
# GeoJSON Features
def nodesToFeatures(nodes):
    """
    :param nodes
    :type nodes from overpy.Result (result.nodes)
    :return:
    """
    features = []
    for node in nodes:
        features.append(nodeToFeature(node))
    return features


# Setup some base data locations

BASE_DIR = os.path.join(os.path.abspath('.'), 'work-flow')
URBAN_BOUNDARIES_FILE = '03_Europe_Capital_10m_urban_boundaries_attrs.geojson'

URBAN_BOUNDARIES_PATH = os.path.join(BASE_DIR,URBAN_BOUNDARIES_FILE)
POIS_PATH            = os.path.join(BASE_DIR, "pois.json")

OVERPASS_API = overpy.Overpass()

geo_df = GeoDataFrame.from_file(URBAN_BOUNDARIES_PATH)

# data frame with geometry
geo_df.columns
geo_df.index
geo_df.ix[0]
geo_sub = geo_df

pois = []

# we will load the
for index, row in geo_sub.iterrows():
    payload = """
        [out:json][timeout:40];
        (
          node["tourism"="gallery"]%(box)s;
          node["tourism"="artwork"]%(box)s;
          node["tourism"="museum"]%(box)s;
        );
        out body;""" % {'box': str(bbox(row.geometry.bounds))}
    # print row.NAME
    # print payload
    result = OVERPASS_API.query(payload)
    pois.extend(nodesToFeatures(result.nodes))


    # artworks  =  filter(lambda n: n.tags['tourism'] == 'artwork', result.nodes)
    # galleries =  filter(lambda n: n.tags['tourism'] == 'gallery', result.nodes)
    # museums   =  filter(lambda n: n.tags['tourism'] == 'museum', result.nodes)

# collect
# persist
# analyse

geojson = {
    "type": "FeatureCollection",
    "features": pois
}

with io.open(POIS_PATH, 'w+', encoding='utf-8') as f:
    f.write(unicode(json.dumps(geojson, ensure_ascii= False)))
