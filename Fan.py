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
#Create setter methods
