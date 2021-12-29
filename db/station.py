class Station:
    __type = ''
    __latitude = 0
    __longitude = 0
    __name = ''

    def __init__(self, type, lat, long, name):
        self.__type = type
        self.__latitude = lat
        self.__longitude = long
        self.__name = name

    def get_type(self):
        return self.__type

    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    def get_name(self):
        return self.__name
