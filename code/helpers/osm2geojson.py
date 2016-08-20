### Helper functions

# given shapely bounds return bbox compatiable with overpass turbo openstreetmap API
def bbox(bounds):
    return (bounds[1],bounds[0],bounds[3],bounds[2])

# given an openstreetmap node retrun a GeoJSON feature
def nodeToFeature(node):
    properties = node.tags
    properties['wkt'] = Point(node.lon, node.lat).wkt
    return {
        "type": "Feature",
        "properties": properties,
        "geometry": {
            "type": "Point",
            "coordinates": [
                float(node.lon),
                float(node.lat)
            ]
        }
    }

# given an array of nodes return an array of GeoJSON features
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

def waysToFeatures(ways):
    print ways
    features = []
    return features
