
import math
class point:
    #constractor
    def __init__(self,a,b):
        self.__w=a
        self.__z=b   
        
    #get w
    def getw(self):
        return self.__w
    #set w
    def setw(self,w):
        self.__w = w
    #get z
    def getz(self):
        return self.__z 
    #get z
    def setz(self,z):
        self.__z = z
        
#نمایش مختصات نقطه
    def __str__ (self):
        return f"({self.__w},{self.__z})"
#جمع دو نقطه
    def __add__ (self,point):
        return point(self.__w+point.getw(),self.__z+point.getz())
#تفریق دو نقطه از هم
    def __sub__ (self,point):
        a_1,a_2=self.__w , point.getw()
        b_1,b_2=self.__z , point.getz()
        return  point(a_1-a_2,b_1-b_2)  
#فاصله دو نقطه از هم
    def distanceFrom(self,point):
        return math.sqrt((self.__w-point.getw())**2+(self.__z-point.getz())**2)
#نعیین که نقطه در کدام ناحیه است
    def whichArea(self):
        a = self.__w
        b = self.__z
        if a>0 and b>0:
            return "1"
        if a>0 and b<0:
            return "4"
        if a<0 and b<0:
            return "3"
        if a<0 and b>0:
            return "2"
        if a == 0 and b>0:
            return  "-1"
        if a == 0 and b<0:
            return  "-1"  
        if a>0 and b == 0:
            return "-1"  
        if a<0 and b == 0:
            return "-1"
        else : return "-1"
