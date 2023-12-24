# backends to be enabled
BACKENDS = [
    'gigaset.backends.local',
#    'gigaset.backends.dastelefonbuch',
    'gigaset.backends.dasoertliche',
]

# own countrycode
COUNTRY = 'DE'

# own area code
AREACODE = '030'

# enable/disable debug messages
DEBUG = False

# port for listening network socket
PORT=12345

# MQTT enable flag
MQTT = True
MQTT_HOST = ""
MQTT_PORT = 123
MQTT_USER = ""
MQTT_PASS = ""