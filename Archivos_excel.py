import pandas as pd
from tabulate import tabulate
# -----------------MOZOS DATA ----------------------#
archivoMozos = "Mozos.xlsx"
data_mozos = pd.read_excel(archivoMozos)
#-------------------MEZAS DATA ---------------------#
archivo_mesas = "Mesas.xlsx"
data_mesas = pd.read_excel(archivo_mesas)
#---------------------------------------------------#


class Mesas:
    def __init__(self,numeroMesa = 0, zonaMesa =str , capacidad=0, estado_mesa =str):
        self.__numeroMesa = numeroMesa
        self.__zonaMesa = zonaMesa
        self.__capacidad = capacidad
        self.__estado = estado_mesa
        
    @property
    def numeroMesa(self):
        return self.__numeroMesa
    
    @numeroMesa.setter
    def numeroMesa(self, numero):
        self.__numeroMesa = numero
    
    @property
    def zonaMesa(self):
        return self.__mesa
    @property
    def capacidas(self):
        return self.__capacidad
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
      
    
    # Metodos de la clase mesas
    def mostrarMesas(self):
        print(tabulate(data_mesas, headers = "keys", tablefmt = "grid"))
    
    def liberar_mesas(self):
        pass
        

class Mozos:
    def __init__(self, idMozo =str, nombre = str, telefono = str,estado = str):
        self.__idMozo = idMozo
        self.__nombre = nombre
        self.__telefono  = telefono
        self.__estado = estado 
        self.__capacidad = 4
    
    @property
    def idMozo(self):
        return self.__idMozo
    @property
    def nombre(self):
        return self.__nombre
    @property
    def telefono(self):
        return self.__telefono
    @property
    def estado (self):
        return self.__estado
    
    @estado.setter
    def estado (self, estado ):
        self.__estado = estado
        
    # Metodos de la clase mozos
    def mostrar_mosos(self):
        print(tabulate(data_mozos, headers = "keys" , tablefmt = "grid"))
        
    def asignar_mozo(self):
        pass
    
    def cambiar_mozo(self):
        pass
    
    
class Restaurante:
    
    def __init__(self, Mozos, Mesas):
        self.__mozos = Mozos
        self.__Mesas = Mesas
    
    @property
    def mosos (self):
        return self.__mozos
    
    @property
    def mesas (self):
        return self.__Mesas
    def guardar_mesas (self,numero_mesa, zona_mesa,capacidad_mesa,estado_mesa):
        archivo_mesas = "Mesas.xlsx"
        data_mesas = pd.read_excel(archivo_mesas)
        nueva_mesa = {
            "numero_mesa": numero_mesa,
            "zona_mesa": zona_mesa,
            "capacidad_mesa": capacidad_mesa,
            "estado_mesa":estado_mesa
        }
        
        data_mesas = pd.concat([data_mesas, pd.DataFrame([nueva_mesa])], ignore_index=True)
        data_mesas.to_excel("Mesas.xlsx", index= False)
    
    def guardar_mozos (self,idMozo, nombre , telefono ,estado ):
        archivoMozos = "Mozos.xlsx"
        data_mozos = pd.read_excel(archivoMozos)
        
        pass 
    
    
    
    
    
    def registrar_mesas(self):
        print("Registro de mesas".center(80, "-"))
        print("-" * 80)
        
        # Ingresamos el numero de mesa
        #   | numero_mesa | zona_mesa | capacidad_mesa | estado_mesa  --> Nombres de la tabla de datos
        while True:
            try:
                numero_mesa = int(input("Ingrese el numero de mesa a registrar (1 - 100): "))
                if 1<= numero_mesa <= 100:
                    if numero_mesa in data_mesas["numero_mesa"].values:
                        print("Error, la mesa ya  esta registrada")
                        return
                    else:
                        break
                else:
                    print("Error, el numero de mesa esta fuera de rango")
            except ValueError:
                print("Error en los datos de ingreso")
        while True:
            zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (sala/terraza): ").lower()
            if zona_mesa in ["sala", "terraza"]:
                break
            else:
                print("Error, la zona de registro no es correcta")
        while True:
            try:
                capacidad_mesa = int(input("Ingrese la capacidad de la mesa ( 1 - 4): "))
                if 1<= capacidad_mesa <= 4:
                    break
                else:
                    print("Error, la capacidad de la mesa no es correcta")
            except ValueError:
                print("Error en los datos de ingreso")
        
        while True:
            estado_mesa = input("Ingrese el estado de la mesa (libre/ocupada/reservada): ").lower()
            if estado_mesa in ["libre", "ocupada", "reservada"]:
                break 
            else:
                print("Error, el estado de mesa no es correcto")
        
        self.guardar_mesas(numero_mesa, zona_mesa,capacidad_mesa,estado_mesa)
        print("-" * 80)
        print("Mesa registrada correctamente".center(80))
        print("-" * 80)
        
        
    def registrar_mozos (self):
        pass
    

def menu():
    print("--" * 30)
    print("<< MENU PRINCIPAL >>".center(60))
    print("--" * 30)
    print("[1] Registrar mesa y mozo    ") 
    print("[2] Solicitar mozo           ")
    print("[3] Tomar pedido             ")
    print("[4] Calcular pago            ")
    print("[5] Ver reportes             ")
    print("[6] Salir  ")
    print("--" * 30)
    print("<< ...SISTEMA RESTAURANTE -- BIENVENIDOS ...>>".center(60))
    print("--" * 30)
    
def main():
    mesas = Mesas ()
    mozos = Mozos()
    restaurante = Restaurante(mesas,mozos)
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if 1 <= opcion <= 7:
                    break
                else:
                    print("Opción invalida. Intente nuevamente.")
            except ValueError:
                print("Entrada invalida. Por favor, ingrese un numero.") 
        
        if opcion == 6:
            print("Saliendo del sistema...")
            break
          
        if opcion == 1:
            while True:
                print("----------------------------------------")
                print("1. Registrar mesas")
                print("2. Registrar mozos")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if 1 <= subopcion <= 3:
                        if subopcion == 1:   
                            restaurante.registrar_mesas()
                        elif subopcion == 2:
                            pass
                        elif subopcion == 3:
                            break
                        else:
                            print("Opcion invalida. Intente nuevamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
                
        elif opcion == 2:  # Asignar mozo a mesa
            while True:
                print("----------------------------------------")
                print("1. Asignar mozo a mesa")
                print("2. Cambiar mozo de la mesa actual")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                       pass
                    elif subopcion == 2:
                        pass
                    elif subopcion == 3:
                        print("Saliendo del menú de mozos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción invalida. Intente nuevamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
                    
        elif opcion == 5: # Aqui se muestran los reportes de los mozos , mesas y los pedidos de los clientes
            while True:
                print("1. Mostrar mesas")
                print("2. Mostrar mozos")
                print("3. Mostrar pedidos clientes")
                print("4. Mostrar pagos realizados")
                print("5. Mostrar mozo con mas pedidos")
                print("6. Mostrar promedio tiempo espera")
                print("7. Pedidos tardios")
                print("8. Mostrar mesa mayor consumo")
                print("9. Mostrar ingresos por zona (sala/Terrasa)")
                print("0. salir")
                try:
                    subopcion = int(input("Seleccione una opcion ( 0 salir ): "))
                    if subopcion == 0:
                        break
                    
                    elif subopcion == 1:
                        mesas.mostrarMesas()
                    elif subopcion == 2:
                        mozos.mostrar_mosos()
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
        
        elif opcion == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida. Por favor, intente nuevamente.")
main()