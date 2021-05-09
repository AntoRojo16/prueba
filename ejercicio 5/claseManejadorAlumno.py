from claseAlumno import Alumno
import csv
class Manejador:
    def __init__ (self):
        self.__lista=[]
        
    def  agregarAlumno (self,alumno):
        self.__lista.append(alumno)
        
    def testAlumno (self):
        archivo=open("Alumno.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                nom=fila[0]
                año=fila[1]
                div=fila[2]
                can=fila[3]
                unAlumno=Alumno(nom,año,div,can)
                self.agregarAlumno(unAlumno)
        archivo.close()
        
        
    def listar (self,año,div):
        lon=len(self.__lista)
        i=0
        for i in range(lon):
            unAlumno=self.__lista[i]
            a=unAlumno.getAño()
            d=unAlumno.getDiv()
            if (año==int(a))and(div==int(d)):
                print(self.__lista[i])
                
    def porcentajeIna (self,año,div):
        #k=self.__lista[i].getCantTot()
        i=0
        long=len(self.__lista)
        print("Alumno     Porcentaje")
        for i in range(long):
            unAlumno=self.__lista[i]
            a=unAlumno.getAño()
            d=unAlumno.getDiv()
            if (int(año)==int(a))and(int(div)==int(d)):
                ina=unAlumno.getIn()
                inM=unAlumno.getCantMax()
                if(int(ina)>int(inM)):
                    alum=unAlumno.getNom()
                    tot=unAlumno.getCantTot()
                    por=int((int(ina)*100)/tot)
                    print ("{:<11}{}%".format(alum,por))
            
            
        
        

            
          
                    
        
    def mostrar (self):
        unAlumno=self.__lista[0]
        print (unAlumno)


#if __name__=="__main__":
 #   unManejador=Manejador()
  #  unManejador.testAlumno()
   # unManejador.listar(2,2)
    #unManejador.mostrar()