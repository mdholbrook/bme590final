from pymodm import MongoModel, fields, connect

"""
    Fields for database:
        -user's email address --> String (primary key)
        -dictionary with:
            -previously selected modes of postprocessing as keys -->
            list of whatever data type that ends up being
            -list as value with:
                -frequency of previously selected modes --> int
                -list of latencies (i.e. runtime) of all previous trials of
                said postprocessing action --> list of floats
        -currently uploaded image(s) --> list of ByteStrings
        -timestamp of current request receipt --> String (datetime)
        -currently postprocessed image(s) --> list of ByteStrings
        -timestamp of current image postprocessing completion --> String
        (datetime)
"""

connect("mongodb://alanr:bme590final@ds241493.mlab.com:41493/bme590final")


class User(MongoModel):
    email = fields.CharField(primary_key=True)
    previousMetrics = fields.DictField()
    uploadedImages = fields.ListField()
    uploadTimestamp = fields.CharField()
    processedImages = fields.ListField()
    processTimestamp = fields.CharField()
    # returnExtension = fields.CharField()
