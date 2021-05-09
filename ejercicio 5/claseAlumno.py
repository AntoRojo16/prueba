class Alumno:
    
    __nom=""
    __año=0
    __div=""
    __cantIn=0
    cantMax=5
    CantTot=80
    
    def __init__ (self,n="nom",a=0,d=0,c=0):
        self.__nom=n
        self.__año=a
        self.__div=d
        self.__cantIn=c
        
    def getNom (self):
        return self.__nom
    
    def getAño (self):
        return self.__año
    
    def getDiv (self):
        return self.__div
    
    def getIn (self):
        return self.__cantIn
    
    @classmethod
    def getCantMax (cls):
        return cls.cantMax
    
    @classmethod
    def getCantTot (cls):
        return cls.CantTot
    
    
    def __str__ (self):
        return ("{}{}{}{}".format(self.__nom,self.__año,self.__div,self.__cantIn))
        

