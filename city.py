class City:
    """
    A container for particular data about city:
    - name - name of the city
    - lat - city's latitude
    - lon - city's longtitude
    - size - city's population size
    - country - two letter country code
    - feature - code indicating city status eg. capital,city, village etc
    - continent - continent, full name
    For full list of city feature codes see: 
    http://www.geonames.org/export/codes.html
    """
    def __init__(self, name, lat, lon, size, country, feature, continent):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.size = size
        self.country = country
        self.feature = feature
        self.continent = continent
    def __str__(self):
        return 'name: ' + self.name + ' latitude:' + str(self.lat) + ' longtitude:' + str(self.lon) + ' population:' + str(self.size) + ' country: ' + str(self.country) + ' feature: ' + str(self.feature) + ' continent: ' + str(self.continent)