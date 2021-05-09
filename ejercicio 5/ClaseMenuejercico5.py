from claseAlumno import Alumno
class Menu:
    __switcher:None
    
    
    def __init__ (self):
        self.__switcher={1: self.opcion1,
                         2: self.opcion2,
                         3: self.salir}
        
    def getSwitcher (self):
        return self.__switcher
    
    
    def opcion (self,op,unManejador):
        func=self.__switcher.get(op, lambda: print("opcion no valida"))
        func(unManejador)
        
    def salir (self,Alumns):
        print("Salir")
        
        
        
    def opcion1 (self,Alumnos):
        a=input("ingrese año  ")
        
        d=input("ingrese division  ")
        if (int(a)<7)and(int(d)<7):
            Alumnos.porcentajeIna(a,d)
        else:
            print("los datos ingresados son incorrectos")
        
        
    def opcion2(self, Alumnos):
        print("MODIFICAR CANTIDAD DE INASISTENCIAS")
        i=input("Ingrese el nuevo valor")
        unAlumno=Alumno()
        t=unAlumno.getCantTot()
        if(int(i)<int(t)):
            Alumno.cantMax=i
            print("Se modifico la cantidad maxima de inasistencias   ")
            c=unAlumno.getCantMax()
            print(c)
        else:
            print("No se puede modificar la cantidad maximas de inasistencias, ya que la cantidad ingresada es mayor que la cantida TOTAl de asistencias")
            
        
        