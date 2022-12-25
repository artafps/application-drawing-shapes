# Auto detect text files and perform LF normalization
# text=auto
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 02:28:03 2022

@author: Hossein782
@author: artafallahpoor
"""

from point import point
class shape:
    def __init__ (self,x=0,y=0,r=0,c=point(0,0),color="rgb(125,125,125)"):
        self.__x=x
        self.__y=y
        self.__r=r
        self.__c=c
        self.__color=color
        if(self.__r>0):
            self.__type='circle'
        elif self.__x>0 and self.__y>0:
            self.__type='square'  
        else :
            self.__type=""  
    def getx (self):
        return self.__x
    def gety (self):
        return self.__y
    def getr (self):
        return self.__r
    def getc (self):
        return self.__c
    def getcolor (self):
        return self.__color
    def gettype (self):
        return self.__type

    def __str__(self):
        if self.__type== "":
            return "\nnot shape"
        if self.__type == "circle":
            return f"\ntype={self.__type}\nr={self.__r}\ncenter=point{self.__c}\ncolor={self.__color}"  
        else:    
            return f"\ntype={self.__type}\nx={self.__x}\ny={self.__y}\ncenter=point{self.__c}\ncolor={self.__color}"  
    #محاسبه مساحت
    def area (self):
        if self.__type == 'circle':
            return(3.14*self.__r*self.__r)
        else:
            return(self.__x*self.__y)
    
    #محاسبه محیط
    def perimeter (self):
        if self.__type =='circle':
            return(2*3.14*self.__r)
        else:
            return (2*self.__x)+(2*self.__y)
    
    #فاصله شکل تا مرکز
    def distance (self):
        return self.__c.distanceFrom(point(0,0))
    
    #فاصله شکل با شکل دیگر
    def distanceFrom (self,shape):
       return self.__c.distanceFrom(shape.getc())
       # return math.sqrt((shape.getc().getw() - self.__c.getw())**2+(shape.getc().getz() - self.__c.getz())**2)

    def isinside (self,shape):
        if (self.__type =='circle') and (shape.gettype() == 'circle'):
            plus = (self.__r)+(shape.getr())
            dplus = self.distanceFrom(shape)
            if (dplus - plus) <= 0:
                return True
            else:
                return False
        if (self.__type =='circle') and (shape.gettype() == 'square'):
            #چهار گوش مستطیل و مربع
            p1=point(shape.getc().getw()-shape.getx()/2,shape.getc().getz()-shape.gety()/2)
            p2=point(shape.getc().getw()-shape.getx()/2,shape.getc().getz()+shape.gety()/2)
            p3=point(shape.getc().getw()+shape.getx()/2,shape.getc().getz()+shape.gety()/2)
            p4=point(shape.getc().getw()+shape.getx()/2,shape.getc().getz()-shape.gety()/2)
            #چهار نقطه وسط اضلاع مستطیل و مربع
            p5=point(shape.getc().getw()-shape.getx()/2,shape.getc().getz())
            p6=point(shape.getc().getw(),shape.getc().getz()+shape.gety()/2)
            p7=point(shape.getc().getw()+shape.getx()/2,shape.getc().getz())
            p8=point(shape.getc().getw(),shape.getc().getz()-shape.gety()/2)
            p9=shape.getc()
            # فاصله نقطه مرکز دایره با 9 نقطه شکل چهارظلعی
            sdp1 = self.__c.distanceFrom(p1) - self.__r
            sdp2 = self.__c.distanceFrom(p2) - self.__r
            sdp3 = self.__c.distanceFrom(p3) - self.__r
            sdp4 = self.__c.distanceFrom(p4) - self.__r
            sdp5 = self.__c.distanceFrom(p5) - self.__r
            sdp6 = self.__c.distanceFrom(p6) - self.__r
            sdp7 = self.__c.distanceFrom(p7) - self.__r
            sdp8 = self.__c.distanceFrom(p8) - self.__r
            sdp9 = self.__c.distanceFrom(p9) - self.__r
            if sdp1<=0 or sdp2<=0 or sdp3<=0 or sdp4<=0 or sdp5<=0 or sdp6<=0 or  sdp7<=0 or  sdp8<=0 or  sdp9<=0 :
                return True
            else: 
                return False
            
            
        if (self.__type =='square') and (shape.gettype() == 'circle'):
            #چهار گوش مستطیل و مربع
            p1=point(self.__c.getw()-self.__x/2,self.__c.getz()-self.__y/2)
            p2=point(self.__c.getw()-self.__x/2,self.__c.getz()+self.__y/2)
            p3=point(self.__c.getw()+self.__x/2,self.__c.getz()+self.__y/2)
            p4=point(self.__c.getw()+self.__x/2,self.__c.getz()-self.__y/2)
            #چهار نقطه وسط اضلاع مستطیل و مربع
            p5=point(self.__c.getw()-self.__x/2,self.__c.getz())
            p6=point(self.__c.getw(),self.__c.getz()+self.__y/2)
            p7=point(self.__c.getw()+self.__x/2,self.__c.getz())
            p8=point(self.__c.getw(),self.__c.getz()-self.__y/2)
            p9=self.__c
            # فاصله نقطه مرکز دایره با 9 نقطه شکل چهارظلعی
            sdp1 = shape.getc().distanceFrom(p1) - shape.getr()
            sdp2 = shape.getc().distanceFrom(p2) - shape.getr()
            sdp3 = shape.getc().distanceFrom(p3) - shape.getr()
            sdp4 = shape.getc().distanceFrom(p4) - shape.getr()
            sdp5 = shape.getc().distanceFrom(p5) - shape.getr()
            sdp6 = shape.getc().distanceFrom(p6) - shape.getr()
            sdp7 = shape.getc().distanceFrom(p7) - shape.getr()
            sdp8 = shape.getc().distanceFrom(p8) - shape.getr()
            sdp9 = shape.getc().distanceFrom(p9) - shape.getr()
            if sdp1<=0 or sdp2<=0 or sdp3<=0 or sdp4<=0 or sdp5<=0 or sdp6<=0 or  sdp7<=0 or  sdp8<=0 or  sdp9<=0 :
                return True
            else: 
                return False
        if (self.__type =='square') and (shape.gettype() == 'square'):
            #self
            #چهار گوش مستطیل و مربع
            fp1=point(self.__c.getw()-self.__x/2,self.__c.getz()-self.__y/2)
            fp2=point(self.__c.getw()-self.__x/2,self.__c.getz()+self.__y/2)
            fp3=point(self.__c.getw()+self.__x/2,self.__c.getz()+self.__y/2)
            fp4=point(self.__c.getw()+self.__x/2,self.__c.getz()-self.__y/2)
            #چهار نقطه وسط اضلاع مستطیل و مربع
            fp5=point(self.__c.getw()-self.__x/2,self.__c.getz())
            fp6=point(self.__c.getw(),self.__c.getz()+self.__y/2)
            fp7=point(self.__c.getw()+self.__x/2,self.__c.getz())
            fp8=point(self.__c.getw(),self.__c.getz()-self.__y/2)
            fp9=self.__c
            #shape
            #چهار گوش مستطیل و مربع
            sp1=point(shape.getc().getw()-shape.getx()/2,shape.getc().getz()-shape.gety()/2)
            sp2=point(shape.getc().getw()-shape.getx()/2,shape.getc().getz()+shape.gety()/2)
            sp3=point(shape.getc().getw()+shape.getx()/2,shape.getc().getz()+shape.gety()/2)
            sp4=point(shape.getc().getw()+shape.getx()/2,shape.getc().getz()-shape.gety()/2)
            #چهار نقطه وسط اضلاع مستطیل و مربع
            sp5=point(shape.getc().getw()-shape.getx()/2,shape.getc().getz())
            sp6=point(shape.getc().getw(),shape.getc().getz()+shape.gety()/2)
            sp7=point(shape.getc().getw()+shape.getx()/2,shape.getc().getz())
            sp8=point(shape.getc().getw(),shape.getc().getz()-shape.gety()/2)
            sp9=shape.getc()
            shape_points1=[fp1,fp2,fp3,fp4,fp5,fp6,fp7,fp8,fp9]
            shape_points2=[sp1,sp2,sp3,sp4,sp5,sp6,sp7,sp8,sp9]
            for i in shape_points1:
                if sp1.getw()<=i.getw() and sp3.getw()>=i.getw() and sp1.getz()<=i.getz() and sp3.getz()>=i.getz() :
                    return True
            for i in shape_points2:
                if fp1.getw()<=i.getw() and fp3.getw()>=i.getw() and fp1.getz()<=i.getz() and fp3.getz()>=i.getz() :
                    return True    
            return False