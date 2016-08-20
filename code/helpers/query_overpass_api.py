# method to handle OverpassTooManyRequests exception from OpenStreetMap/overpass turbo API
def retry_if_overpass_too_many_requests(exception):
    return isinstance(exception, overpy.exception.OverpassTooManyRequests)

# decorator to retry with exponential back off
@retry(wait_exponential_multiplier=2000,
       wait_exponential_max=60000,
       retry_on_exception=retry_if_overpass_too_many_requests)
def call_overpass_api(q):
    return OVERPASS_API.query(q)

def run_overpass_api(bounding_geo_df):
    local_pois = []
    for index, row in bounding_geo_df.iterrows():
        # For documentation see:
        # http://wiki.openstreetmap.org/wiki/Tag:{key}={value}
        # e.g: http://wiki.openstreetmap.org/wiki/Tag:amenity=theatre
        payload = """
            [out:json][timeout:60];
            (
              node["tourism"="gallery"]%(box)s;
              node["tourism"="artwork"]%(box)s;
              node["tourism"="museum"]%(box)s;
              node["amenity"="arts_centre"]%(box)s;
              node["amenity"="theatre"]%(box)s;
            );
            out body;""" % {'box': str(bbox(row.geometry.bounds))}
        result = call_overpass_api(payload)
        local_pois.extend(nodesToFeatures(result.nodes))
