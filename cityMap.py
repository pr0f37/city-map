if __name__ == '__main__':
    import sys
    import mapReader
    import mapPainter
    dbFile = ''
    mapFile = ''
    cities = 20
    attNum = (len(sys.argv[1:]))
    capitals = []
    
    if attNum < 2 or attNum > 3:
        print 'Insufficient number of attributes, please try again'
    else:
        if (len(sys.argv[1:])) == 3:
            dbFile = sys.argv[1]
            mapFile = sys.argv[2]
            cities = int(sys.argv[3])
        elif (len(sys.argv[1:])) == 2:
            dbFile = sys.argv[1]
            mapFile = sys.argv[2]
        print 'Attribute values: dbFile=', dbFile, 'mapFile=', mapFile, 'cities=', cities
        
        mr = mapReader.MapReader()
        mr.read_database(dbFile)
        
        countries = ['PL', 'US', 'FR', 'GB']
        c = mr.get_cities_from_countries(mr.get_countries(), cities)
        # for city in c:
        #     print city
        # for size in sorted(mr.citiesDict.keys(), reverse = True):
        #     if mr.citiesDict[size].feature == 'PPLC' and cities > 0:
        #         capitals.append(mr.citiesDict[size])
        #         cities -= 1
        mp = mapPainter.MapPainter(mapFile)
        mp.draw_map(c, (3135,2945))