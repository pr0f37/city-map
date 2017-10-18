class MapPainter:
    """
    Class used for creating an image file presenting chosen cities as dots 
    located on map - size of the dot is corresponding to city's population.
    """
    def __init__(self, fname):
        from PIL import Image
        try:
            self.fname = fname
            self.map_deg = 360.0
            im = Image.open(fname)
            self.map_area = im.size[0] * im.size[1]
            del im
        except IOError:
            print 'Map image file does not exist'
    """
    Function computing radius of a cicrle indicating city on the map view
    """
    def get_city_radius(self, city_size):
        from math import sqrt
        radius = sqrt(self.map_area * 0.00004) / 2
        if city_size > 10000000:
            return radius
        if city_size > 5000000:
            return 0.7 * radius
        if city_size > 1000000:
            return 0.5 * radius
        if city_size > 100000:
            return 0.25 * radius
        if city_size > 10000:
            return 0.1 * radius
        return 0.05 * radius
    """
    Function returning color used to draw a circle indicating city on the map view. Color is dependant on the city type
    """
    def get_city_color(self, city_feature):
        if city_feature == 'PPLC':
            return 'rgb(255,0,0)'
        if city_feature == 'PPLA':
            return 'rgb(255, 127, 0)'
        if city_feature == 'PPLA2':
            return 'rgb(255, 192, 0)'
        if city_feature == 'PPLA3':
            return 'rgb(255, 220, 0)'
        if city_feature == 'PPLA4':
            return 'rgb(255, 255, 0)'
        return 'rgb(0,255,0)'
    """
    Function converting map coordinates to image coordinates
    """
    def map_cord_to_canv_cord(self, city, center_point, image_width):
        from math import log, tan, radians, pi
        x = center_point[0] + float(city.lon) * (image_width/self.map_deg)
        merc = log(tan(pi/4 + radians(city.lat)/2))
        y = (center_point[1] - (image_width*merc/(2*pi)))
        return [x, y]
    """
    Procedure used to draw cities in given image
    """
    def draw_map(self, cities, point_zero = 0.0):
        from PIL import Image, ImageDraw   
        try:
            im = Image.open(self.fname)
            im = im.convert('RGB')
            if point_zero == 0.0:
                point_zero = (im.size[0]//2, im.size[1]//2)
            draw = ImageDraw.Draw(im)
            for city in cities:
                x, y = self.map_cord_to_canv_cord(city, point_zero, im.size[0])
                radius = self.get_city_radius(city.size)
                color = self.get_city_color(city.feature)
                draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill = color)
            del draw
            im.save(self.fname[:len(self.fname) - 4] + '_q.jpg')
            del im
        except IOError:
            pass