class MapReader:
    """
    Class used for reading a database file
    """
    def __init__(self):
        self.cities = []
        self.citiesDict = {}
    """
    Checks wether given argument is float
    return  True if argument is float
            False otherwise
    """
    def is_float(self, st):
        try:
            float(st)
            return True
        except Exception:
            return False
    """
    Checks wether given argument is int
    return  True if argument is float
            False otherwise
    """
    def is_int(self, st):
        try:
            int(st)
            return True
        except Exception:
            return False
    """
    Reads standard geonames database file, parses it and creates cities dictionary.
    See City class (./city.py)
    """
    def read_database(self, fname):
        import city
        with open(fname, 'r') as f:
            for line in f.readlines():
                cityData = line.split('\t')
                if (self.is_float(cityData[4]) and self.is_float(cityData[5]) and self.is_int(cityData[14])):
                    c = city.City(cityData[2], float(cityData[4]), (cityData[5]), int(cityData[14]), cityData[8], cityData[7], cityData[17].split('/')[0])
                    if c.feature != 'PPL':
                        self.cities.append(c)
                        self.citiesDict[c.size] = c
                else:
                    print repr(line)
    """
    Reads standard geonames database file, parses it and print parsed cities with 
    argument numbers. Created for debugging reasons
    """
    def print_database(self, fname):
        with open(fname, 'r') as f:
            for line in f.readlines():
                cityData = line.split('\t')
                i = 0
                for data in cityData:
                    print 'cityData[',i ,']', data,';'
                    i = i + 1
                ok = raw_input("")
    """
    Filters dictionary by category and gives n biggest cities
    """
    def get_filtered_database(self, mode, type, limit = 20):
        cities = []
        for size in sorted(self.citiesDict, reverse = True):
            if (limit > 0 and
                        ((self.citiesDict[size].feature == type and mode in['i', 'include'])
                        or
                        ((self.citiesDict[size].feature != type and mode in['e', 'exclude'])))):
                cities.append(self.citiesDict[size])
                limit -= 1
        return cities
    """
    Returns updated information about cities given in cities list
    """
    def get_cities_from_list(self, cityNames):
        cities = []
        for city in cityNames:
            for size in sorted(self.citiesDict, reverse = True):
                if self.citiesDict[size].name.lower().count(city.lower()) > 0:
                    cities.append(self.citiesDict[size])
                    break
        return cities
    """
    Returns up to @limit number of biggest cities for each country in @countries list.
    """
    def get_cities_from_countries(self, countries, limit):
        cities = []
        countriesDict = {}
        for country in countries:
            countriesDict[country.lower()] = limit
        for size in sorted(self.citiesDict, reverse = True):
            if self.citiesDict[size].country.lower() in countriesDict and countriesDict[self.citiesDict[size].country.lower()] > 0:
                cities.append(self.citiesDict[size])
                countriesDict[self.citiesDict[size].country.lower()] -= 1
        return cities
    """
    Returns countries list 
    """
    def get_countries(self):
        countries = []
        for size in sorted(self.citiesDict, reverse = True):
            if self.citiesDict[size].country not in countries:
                countries.append(self.citiesDict[size].country)
        return countries