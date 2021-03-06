#encoding:UTF-8
#Lenin Silva Gutiérrez A01373214
#Ciclos while

def recolectarInsectos(): #Función para recolectar insectos
    insectos=0
    dias=0
    while insectos<30: #Detiene el loop si hay 30 insectos o más
        recolectados=int(input("Insectos recolectados hoy")) #Lee los insectos recolectados
        insectos+=recolectados #Va sumando los insectos obtenidos
        dias+=1 #Cuenta los días transcurridos
        if insectos<=30: #Supuesto de que no ha llegado a la meta o junto exactamente 30
            print ("""Después de %d días(s) de recolección, has acumulado 
%d insectos. Te hace falta recolectar %d insectos"""%(dias,insectos,30-insectos))
        else: #Supuesto de que se pasó de la meta
            print("""Después de %d día(s) de recolección, has acumulado
%d insectos. Te pasaste por %d insectos"""%(dias, insectos, insectos-30))
        print("")
       
    print ("¡Felicidades! Has llegado a la meta")

def encontrarMayor():
    datos=int(input(""""Salir: -1
Valor entero positivo""")) #Lee los datos

    mayor=0
    while datos!=-1: #Mientras no seleccionen salir
        if datos>0:
            print(datos) #Imprime el dato sólo si es un entero positivo
        if datos>mayor:
            mayor=datos #Si el dato es mayor que el anterior, se cambia el valor del mayor
            
        datos=int(input("""Salir: -1
Valor entero positivo""")) #Pide nuevamente la entrada
            
    if mayor==0: #Supone que no se metió ningún dato válido
        print("No hay datos para encontrar el mayor")
    else:
        print ("El mayor es: %d"%mayor)#imprime el número mayor
              

def main():
    opcion=int(input("""1. Encontrar mayor
2. Recolectar insectos
3. Salir
Teclea tu opción""")) #Lee la opción del usuario

    while opcion<1 or opcion>3: #Solicita nuevamente la entrada si no es vlida 
        print ("Selecciona una opción válida")
        opcion=int(input("""1. Encontrar mayor
2. Recolectar insectos
3. Salir
Teclea tu opción"""))

    while opcion==1 or opcion==2: #Si se elige una opción válida, el programa corre
        if opcion==1:
            encontrarMayor()#Ejecuta el programa para encontrar el mayor
        else:
            recolectarInsectos()#Ejecuta el programa para la recolección de insectos
            
        opcion=int(input("""1. Encontrar mayor
2. Recolectar insectos
3. Salir
Teclea tu opción""")) #Lee nuevamente la entrada del usuario

        while opcion<1 or opcion>3: #Solicita nuevamente la entrada si no es válida
            print ("Selecciona una opción válida")
            opcion=int(input("""1. Encontrar mayor
2. Recolectar insectos
3. Salir
Teclea tu opción"""))

    print ("Vuelve pronto") #Se despide del usuario
    
main()

     