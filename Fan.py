#Create a class named fan
class Fan:
#Create three constants to represent a fan
    SLOW = 1
    MEDIUM = 2
    FAST = 3
#Set the default values    
    def __init__(self, fanspeed = SLOW, fanradius = 5.00, fancolor = 'blue', fanon=False):
        self.__fanspeed = fanspeed
        self.__fanon = fanon
        self.__fanradius = fanradius
        self.__fancolor = fancolor
#Create getter methods
    def get_fanspeed(self):
        return self.__fanspeed

    def get_fanon(self):
        return self.__fanon

    def get_fanradius(self):
        return self.__fanradius

    def get_fancolor(self):
        return self.__fancolor
#Create setter methods
    def set_fanspeed(self, fanspeed):
        self.__fanspeed = fanspeed
    
    def set_fanon(self, fanon):
        self.__fanon = fanon

    def set_fanradius(self, fanradius):
        self.__fanradius = fanradius

    def set_fancolor(self, fancolor):
        self.__fancolor = fancolor
