import pandas as pd
from tabulate import tabulate
# -----------------MOZOS DATA ----------------------#
archivoMozos = "Mozos.xlsx"
data_mozos = pd.read_excel(archivoMozos)
#-------------------MEZAS DATA ---------------------#
archivo_mesas = "Mesas.xlsx"
data_mesas = pd.read_excel(archivo_mesas)
#---------------------------------------------------#

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
    def guardar_mesas (self,mesa):
        archivo_mesas = "Mesas.xlsx"
        data_mesas = pd.read_excel(archivo_mesas)
        nueva_mesa = {
            "numero_mesa": mesa.numeroMesa,
            "zona_mesa": mesa.zonaMesa,
            "capacidad_mesa": mesa.capacidad,
            "estado_mesa": mesa.estado
        }
        
        data_mesas = pd.concat([data_mesas, pd.DataFrame([nueva_mesa])], ignore_index=True)
        data_mesas.to_excel("Mesas.xlsx", index= False)
    
      #|id_mozo | nombre|telefono | estado |mesas_reservadas
    def guardar_mozos (self,mozo):
        archivoMozos = "Mozos.xlsx"
        data_mozos = pd.read_excel(archivoMozos)
        nuevo_mozo = {
            "id_mozo": mozo.idMozo,
            "nombre": mozo.nombre,
            "telefono": mozo.telefono,
            "estado": mozo.estado,
            "mesas_reservadas": []
        }
        
        data_mozos = pd.concat([data_mozos,pd.DataFrame([nuevo_mozo])], ignore_index= True)
        data_mozos.to_excel("Mozos.xlsx", index=False)
        
        
    
    # ?------------------------------------------------------------------------------
    def reporte_registros(self):
        # Mostrar el reporte de mesas registradas
        print("-" * 80)
        print("MESAS REGISTRADAS".center(80))
        print("Terraza: ", len(data_mesas[data_mesas["zona_mesa"] == "Terraza"] ["numero_mesa"].tolist()), "mesas")
        print("Sala   : ", len(data_mesas[data_mesas["zona_mesa"] == "Sala"]["numero_mesa"].tolist()), "mesas")
        print("TOTAL DE REGISTROS PERMITIDOS POR EL RESTAURANTE: 50 MESAS")
        print("20 MESAS EN TERRAZA Y 30 MESAS EN SALA".center(56))
        print("-" * 80)
    # ?------------------------------------------------------------------------------
        
        

    def registrar_mesas(self):
        # Ingresamos el numero de mesa
        #   | numero_mesa | zona_mesa | capacidad_mesa | estado_mesa  --> Nombres de la tabla de datos
        print("Registro de mesas".center(80, "-"))
        while True:
            try:
                numero_mesa = int(input("Ingrese el numero de mesa a registrar (1 - 50): "))
                if 1<= numero_mesa <= 50:
                    if numero_mesa in data_mesas["numero_mesa"].values:
                        print("Error, la mesa ya  esta registrada")
                        return
                    else:
                        break
                else:
                    print("Error, el numero de mesa esta fuera de rango (50 mesas maximo)")
            except ValueError:
                print("Error en los datos de ingreso")
        while True:
            zona_mesa = input("Ingrese la zona de disponibilidad de la mesa (Sala/Terraza): ").title()
            if zona_mesa in ["Sala", "Terraza"]:
                break
            else:
                print("Error, la zona de registro no es correcta")
                
                
                
        # ?------------------------------------------------------------------------------
        # Validamos la zona de la mesa
        if zona_mesa == "Sala":
            if len(data_mesas[data_mesas["zona_mesa"] == "Sala"]) >= 30:
                print("Error, ya se han registrado 30 mesas en la zona Sala")
                return
        if zona_mesa == "Terraza":
            if len(data_mesas[data_mesas["zona_mesa"] == "Terraza"]) >= 20:
                print("Error, ya se han registrado 20 mesas en la zona Terraza")
                return
        # ?------------------------------------------------------------------------------
        
        
        
        
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
            estado_mesa = input("Ingrese el estado de la mesa (Libre/Ocupada/Reservada): ").title()
            if estado_mesa in ["Libre", "Ocupada", "Reservada"]:
                break 
            else:
                print("Error, el estado de mesa no es correcto")
        mesa = Mesas(numero_mesa, zona_mesa,capacidad_mesa, estado_mesa)
        self.guardar_mesas(mesa)
        print("-" * 80)
        print("Mesa registrada correctamente".center(80))
        print("-" * 80)
    
    
    
    # ?------------------------------------------------------------------------------
    def reporte_mozos(self):
        # Mostrar el reporte de mozos registrados
        print("-" * 80)
        print("MOZOS REGISTRADOS".center(80))
        print("Total de mozos registrados: ", len(data_mozos))
        print("Mozos activos  : ", len(data_mozos[data_mozos["estado"] == "Activo"]))
        print("Mozos inactivos: ", len(data_mozos[data_mozos["estado"] == "Inactivo"]))
        print("-" * 80)
    # ?------------------------------------------------------------------------------
    
        
        
        
        
        
        
        
        
        
        
        
    #|id_mozo | nombre|telefono | estado |mesas_reservadas --> Nombre de datos del mozo
    def registrar_mozos (self):
        print("-" * 80)
        print("Registro de mozos".center(80, "-"))
        print("-" * 80)
        while True:
            existe_mzo = False
            id_mozo = input("Ingrese el id del mozo ( 4 digitos): ")
            if len(id_mozo) == 4 and id_mozo.isdigit():
                if id_mozo in data_mozos["id_mozo"].values:
                    print("Error, el mozo ya esta registrado")
                    return
                else:
                    break
            else:
                print("El id debe ser de 4 digitos numericos")
                
        while True:
            nombre_mozo = input("Ingrese el nombre y apellido del mozo: ")
            contiene_numero = False
            for caracter in nombre_mozo:
                if caracter.isdigit():
                    contiene_numero = True
                    print("El nombre no debe tener numeros")
                    break
            if not contiene_numero:
                break
        
        while True:
            try:
                telefono_mozo = input("Ingrese el telefono del mozo (9 digitos): ")
                if len(telefono_mozo) == 9 and telefono_mozo.isdigit():
                    if telefono_mozo in data_mozos["telefono"].values:
                        print("Error el telefono ya esta registrado")
                    
                    else: 
                        break
                else:
                    print("Error el telefono no es correcto")
            except ValueError:
                print("Error datos de ingreso incorrectos")
        
        while True:
            estado_mozo = input("Ingrese el estado del mozo (Activo/Inactivo) sin espacios: ").title()
            if estado_mozo in ["Activo", "Inactivo"]:
                break
            else:
                print("Error, el estado del mozo no es correcto")
        mozo = Mozos(id_mozo,nombre_mozo, telefono_mozo,estado_mozo)    
        self.guardar_mozos(mozo)
        
        print("-" * 80)
        print("Mozo registrado correctamente".center(80))
        print("-" * 80)

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
        return self.__zonaMesa
    @property
    def capacidad(self):
        return self.__capacidad
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, estado):
        self.__estado = estado
      
    
    # Metodos de la clase mesas
    def mostrarMesas(self):
        df_mesas = pd.read_excel("Mesas.xlsx")
        print(tabulate (df_mesas, headers = "keys", tablefmt = "grid"))
    
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
        
    @property
    def capacidad(self):
        return self.__capacidad
    
    # Metodos de la clase mozos
    def mostrar_mosos(self):
        df_mozos = pd.read_excel("Mozos.xlsx")
        print(tabulate(df_mozos, headers = "keys" , tablefmt = "grid"))
        
        
    def asignar_mozo(self):
        if data_mozos.empty:
            print("No hay mozos registrados")
            return 

        # Validar ID del mozo
        while True:
            idMozo = input("Ingrese el id del mozo a asignar (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")

        # Verificar existencia del mozo
        if idMozo in data_mozos["id_mozo"].astype(str).values:
            mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
            mozo = data_mozos.loc[mozo_index]
        else:
            print("El id del mozo no está registrado")
            return

        # Verificar estado del mozo
        if mozo["estado"] != "Activo":
            print("Error: el mozo no está activo y disponible")
            return

        # Cargar mesas reservadas
        m_reservadas = mozo["mesas_reservadas"]
        if isinstance(m_reservadas, str):
            m_reservadas = eval(m_reservadas)
        else:
            m_reservadas = []

        # Verificar límite de mesas
        if len(m_reservadas) >= 4:
            print("El mozo ya tiene 4 mesas asignadas y ahora está inactivo")
            data_mozos.at[mozo_index, "estado"] = "Inactivo"
            data_mozos.to_excel("Mozos.xlsx", index=False)
            print(f"El mozo {mozo['nombre']} ahora está inactivo.")
            return
        else:
            data_mozos.at[mozo_index, "estado"] = "Activo"
            data_mozos.to_excel("Mozos.xlsx", index=False)
        
        # Asignar mesa
        while True:
            try:
                mesa = int(input("Ingrese el número de mesa a asignar: "))
            except ValueError:
                print("Debe ingresar un número entero")
                continue

            if not (1 <= mesa <= 50):
                print("Error, el número de mesa no es válido (1-100)")
                continue
            
            if str(mesa) not in data_mesas["numero_mesa"].astype(str).values:
                print("El número de mesa no está registrado")
                continue

            if mesa in m_reservadas:
                print("El mozo ya tiene asignada esa mesa, seleccione otra")
                continue

            # Verificar estado de la mesa
            data_mesa = data_mesas[data_mesas["numero_mesa"].astype(str) == str(mesa)]
            if data_mesa.empty:
                print("Error: no hay datos de la mesa")
                continue

            estado_mesa = data_mesa.iloc[0]["estado_mesa"]
            if estado_mesa != "Libre":
                print("La mesa no está libre, seleccione otra")
                continue

            # Todo está correcto, asignar mesa
            m_reservadas.append(mesa)
        
            
        # ?------------------------------------------------------------------------------
            # Actualizar el estado de la mesa a "Reservada"
            data_mesas.loc[data_mesas["numero_mesa"] == mesa, "estado_mesa"] = "Reservada"
            data_mesas.to_excel("Mesas.xlsx", index=False)
        # ?------------------------------------------------------------------------------
        
        
        
            # Actualizar las mesas reservadas del mozo
            data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
            data_mozos.to_excel("Mozos.xlsx", index=False)
            print(f"Mozo {mozo['nombre']} asignado correctamente a la mesa {mesa}.")
            break  # ✅ Salir del bucle luego de asignar

    def eliminar_mesas_asignadas(self):
        if data_mozos.empty:
            print("No hay mozos registrados")
            return
        
        while True:
            idMozo = input("Ingrese el id del mozo (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")
        
        if idMozo in data_mozos["id_mozo"].astype(str).values:
            mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
            m_reservadas = data_mozos.at[mozo_index, "mesas_reservadas"]
            if isinstance(m_reservadas, str):
                m_reservadas = eval(m_reservadas)
            else:
                m_reservadas = []
            
            if not m_reservadas:
                print("El mozo no tiene mesas asignadas")
                return
            
            print(f"Mesas asignadas al mozo {idMozo}: {m_reservadas}")
            
            while True:
                try:
                    mesa = int(input("Ingrese el número de mesa a eliminar de las asignadas: "))
                    if mesa in m_reservadas:
                        m_reservadas.remove(mesa)
                        data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"Mesa {mesa} eliminada de las asignaciones del mozo {idMozo}.")
                        
                        
                        # ? ---------------------------------------------------------------------------------
                        # ACTUALIZAR EL ESTADO DEL MOZO A ACTIVO SI TIENE MENOS DE 4 MESAS ASIGNADAS
                        if len(m_reservadas) < 4:
                            data_mozos.at[mozo_index, "estado"] = "Activo"
                            data_mozos.to_excel("Mozos.xlsx", index=False)
                            print(f"El mozo {idMozo} ahora está activo.")
                        # ACTUALIZAR EL ESTADO DE LA MESA A LIBRE
                        data_mesas.loc[data_mesas["numero_mesa"] == mesa, "estado_mesa"] = "Libre"
                        data_mesas.to_excel("Mesas.xlsx", index=False)
                        break
                        # ? ---------------------------------------------------------------------------------
                        
                    else:
                        print("La mesa no está asignada al mozo.")
                except ValueError:
                    print("Debe ingresar un número entero.")
        else:
            print("El id del mozo no está registrado")
            

    def cambiar_mozo(self):
        if data_mozos.empty:
            print("No hay mozos registrados")
            return
        
        while True:
            idMozo = input("Ingrese el id del mozo a cambiar (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")
        
        if idMozo in data_mozos["id_mozo"].astype(str).values:
            mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
            m_reservadas = data_mozos.at[mozo_index, "mesas_reservadas"]
            if isinstance(m_reservadas, str):
                m_reservadas = eval(m_reservadas)
            else:
                m_reservadas = []
            
            if not m_reservadas:
                print("El mozo no tiene mesas asignadas")
                return
            
            print(f"Mesas asignadas al mozo {idMozo}: {m_reservadas}")
            
            while True:
                try:
                    mesa = int(input("Ingrese el número de mesa a cambiar: "))
                    if mesa in m_reservadas:
                        nuevo_id_mozo = input("Ingrese el nuevo id del mozo (4 dígitos): ")
                        if len(nuevo_id_mozo) == 4 and nuevo_id_mozo.isdigit():
                            if nuevo_id_mozo in data_mozos["id_mozo"].astype(str).values:
                                nuevo_mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == nuevo_id_mozo].index[0]
                                nuevo_m_reservadas = data_mozos.at[nuevo_mozo_index, "mesas_reservadas"]
                                if isinstance(nuevo_m_reservadas, str):
                                    nuevo_m_reservadas = eval(nuevo_m_reservadas)
                                else:
                                    nuevo_m_reservadas = []
                                
                                # Verificar si el nuevo mozo ya tiene 4 mesas asignadas
                                if len(nuevo_m_reservadas) >= self.capacidad:
                                    print(f"El mozo {nuevo_id_mozo} ya tiene 4 mesas asignadas.")
                                    return
                                
                                # Cambiar la mesa
                                nuevo_m_reservadas.append(mesa)
                                m_reservadas.remove(mesa)
                                data_mozos.at[mozo_index, "mesas_reservadas"] = str(m_reservadas)
                                data_mozos.at[nuevo_mozo_index, "mesas_reservadas"] = str(nuevo_m_reservadas)
                                data_mozos.to_excel("Mozos.xlsx", index=False)
                                print(f"Mesa {mesa} cambiada del mozo {idMozo} al mozo {nuevo_id_mozo}.")
                                break
                            else:
                                print("El nuevo id del mozo no está registrado")
                        else:
                            print("Error, el nuevo id del mozo no es correcto")
                    else:
                        print("La mesa no está asignada al mozo.")
                except ValueError:
                    print("Debe ingresar un número entero.")
                    
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
        # ?------------------------------------------------------------------------------
            
            while True:
                print("----------------------------------------")
                print("1. Registrar mesas")
                print("2. Registrar mozos")
                print("3. Reportes de registros mesas por zona")
                print("4. Reportes de registros mozos")
                print("5. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if 1 <= subopcion <= 5:
                        if subopcion == 1:   
                            restaurante.registrar_mesas()
                        elif subopcion == 2:
                            restaurante.registrar_mozos()
                        elif subopcion == 3:
                            restaurante.reporte_registros()
                        elif subopcion == 4:
                            restaurante.reporte_mozos()
                        elif subopcion == 5:
                            break
                        else:
                            print("Opcion invalida. Intente nuevamente.")
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
        # ?------------------------------------------------------------------------------
            
            
            
            
            
        elif opcion == 2:  # Asignar mozo a mesa
            while True:
                print("----------------------------------------")
                print("1. Asignar mozo a mesa")
                print("2. Cambiar mozo de la mesa actual")
                print("3. Eliminar mesa asignada")
                print("4. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                       mozos.asignar_mozo()
                    elif subopcion == 2:
                        mozos.cambiar_mozo()
                    elif subopcion == 3:
                        mozos.eliminar_mesas_asignadas()
                    elif subopcion == 4:
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