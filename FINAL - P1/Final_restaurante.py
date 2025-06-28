import pandas as pd
from tabulate import tabulate
# -----------------MOZOS DATA ----------------------#
archivoMozos = "Mozos.xlsx"
data_mozos = pd.read_excel("Mozos.xlsx")
#-------------------MEZAS DATA ---------------------#
archivo_mesas = "Mesas.xlsx"
data_mesas = pd.read_excel(archivo_mesas)
#---------------------------------------------------#
# -----------------CLIENTES DATA ----------------------#
archivoClientes = "Clientes.xlsx"
data_clientes = pd.read_excel(archivoClientes)


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
    
    def guardar_Cliente (self,cliente):
        archivoClientes = "Clientes.xlsx"
        data_clientes = pd.read_excel(archivoClientes)
        nuevo_Cliente = {
            "id_Cliente": cliente.id_Cliente,
            "num_mesa": cliente.num_mesa,
            "num_mozo": cliente.num_mozo,
            "pedido": [],
            "fecha": cliente.fecha,
            "entregado": cliente.entregado
        }
        
        data_clientes = pd.concat([data_clientes, pd.DataFrame([nuevo_Cliente])], ignore_index=True)
        data_clientes.to_excel("Clientes.xlsx", index=False)
    
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
        
    def existe_mesa (self, numero_mesa):
        if numero_mesa in data_mesas["numero_mesa"].values:
            return True
        else:
            return False
    
    def existe_mozo (self, num_mozo):
        if num_mozo in data_mozos["id_mozo"].values:
            return True
        else:
            return False        

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


    def reportes_clientes(self):
        print("-" * 80)
        print("CLIENTES REGISTRADOS".center(80))
        print("Total de CLIENTES registrados: ", len(data_clientes))
        print("Clientes con su pedido entregado: ", len(data_clientes[data_clientes["entregado"] == "si"]))
        print("Clientes sin su pedido entregado: ", len(data_clientes[data_clientes["entregado"] == "no"]))
        print("-" * 80)
        
        
    #|id_Cliente | num_mesa | num_mozo | pedido | fecha
    def registrar_cliente(self):
        print("-" * 80)
        print("Registro de Clientes".center(80))
        print("-" * 80)
        while True:
            id_Cliente = int(input("Ingrese el id del Cliente (4 digitos): "))
            if len(str(id_Cliente)) == 4:
                if id_Cliente in data_clientes["id_Cliente"].values:
                    print("Error, el Cliente ya esta registrado")
                else:
                    break
            else:
                print("El id debe ser de 4 digitos numericos")
        while True:
            num_mesa = int(input("Ingresar el numero de mesa: "))
            if self.existe_mesa(num_mesa) == False:
                print("la mesa debe estar registrada") 
            else:
                estado_mesa = data_mesas.loc[data_mesas["numero_mesa"] == num_mesa, "estado_mesa"].values[0]
                if estado_mesa == "Libre":
                    print("La mesa esta libre.")
                    break    
                else:
                    print("La mesa ya esta reservada.")
        while True:
            num_mozo = int(input("Ingresar el numero del mozo: "))
            if self.existe_mozo(num_mozo) == False:
                print("El mozo no esta registrado") 
            else:
                estado_mozo = data_mozos.loc[data_mozos["id_mozo"] == num_mozo, "estado"].values[0]
                if estado_mozo == "Activo":
                    print("El mozo está activo.")
                    break  
                else:
                    print("El mozo está inactivo, elija otro mozo.")
        
        while True:
            print("Su pedido a sido entregado?")
            entregado = input(": ").lower()
            if entregado in ["si", "no"]:
                break
            else:
                print("debe ser si o no")
        
        while True:
            opcion = input("Desea agregar un pedido?").upper()
            if opcion == "SI":
                pass
            elif opcion == "NO":
                
                pedido = []
                fecha = "0"
                print("Estaremos en espera de su respuesta")
                break
            else:
                print("Debe ser si o no")

            print("REGISTRO DE PEDIDO")
            #AQUI INGRESAR LA FUNCION DE REGISTRO DE PEDIDO
        
        cliente = Clientes(id_Cliente, num_mesa, num_mozo, pedido, fecha, entregado)    
        self.guardar_Cliente(cliente)
        print("-" * 80)
        print("Cliente registrado correctamente".center(80))
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

    
    
    def eliminar_mesa (self):
        global data_mesas
        
        while True:
            try:
                numero_mesa = int(input("Ingrese el numero de mesa a eliminar(1 - 50): "))
                if 1<= numero_mesa <= 50:
                    if numero_mesa in data_mesas["numero_mesa"].values:
                        break
                    else:
                        print("La mesa no esta registrada en la base de datos")
                else:
                    print("Error, el numero de mesa esta fuera de rango (50 mesas maximo)")
                    
            except ValueError:
                print("Error en los datos de ingreso")
                
        while True:
            respuesta = input(f"Desea eliminar la mesa numero {numero_mesa} (si/no) ?: ").lower()
            if respuesta in ["si", "no"]:
                break 
            else:
                print("Formato de respuesta incorrecto")
        
        if respuesta == "si":
            
            if numero_mesa in data_mesas["numero_mesa"].values:
                data_mesas = data_mesas[data_mesas["numero_mesa"] != numero_mesa]
                print(f"Mesa con numero {numero_mesa} eliminado correctamente")
                data_mesas.to_excel("Mesas.xlsx", index = False)
                
            else:
                print("La mesa no esta registrada")
        else:
            print("Procedo de eliminacon cancelado")
            
    def liberar_mesas(self):
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
    
    def eliminar_mozo (self):
        global data_mozos
        # Validar ID del mozo
        while True:
            idMozo = input("Ingrese el id del mozo a eliminar (4 dígitos): ")
            if len(idMozo) == 4 and idMozo.isdigit():
                break
            else:
                print("Error, el id del mozo no es correcto")   
        while True:
            respuesta = input(f"Desea eliminar el mozo con id {idMozo} (si/no): ").lower()
            if respuesta in ["si", "no"]:
                break 
            else:
                print("Formato de respuesta incorrecto")
                
        if respuesta == "si":
            # Verificar existencia del mozo
            if idMozo in data_mozos["id_mozo"].astype(str).values:
                data_mozos = data_mozos[data_mozos["id_mozo"].astype(str) != idMozo]
                print(f"Mozo con ID {idMozo} eliminado correctamente.")
                data_mozos.to_excel("Mozos.xlsx", index=False)
            else:
                print("El mozo no esta registrado ")
        else:
            print("Proceso de eliminacion cancelado")
    
    def modificar_datos(self):
        while True:
            idMozo = input("Ingrese el id del mozo a asignar (4 dígitos): ")
            if len(idMozo) != 4 or not idMozo.isdigit():
                print("Error, el id del mozo no es correcto")
                continue

            # Verificar existencia del mozo
            if idMozo in data_mozos["id_mozo"].astype(str).values:
                break
            else:
                print("El id del mozo no está registrado")
                return
        
        mozo_index = data_mozos[data_mozos["id_mozo"].astype(str) == idMozo].index[0]
        mozo = data_mozos.loc[mozo_index]
        print("-"*80)
        print(f"Datos actuales del mozo {mozo['nombre']}:")
        print(f"ID      : {mozo['id_mozo']}")
        print(f"Nombre  : {mozo['nombre']}")
        print(f"Teléfono: {mozo['telefono']}")
        print(f"Estado  : {mozo['estado']}")
        print("-"*80)
        while True:
            while True:
                print("MENU DE ACTUALIZACION DE DATOS".center(80, "-"))
                print("1. Modificar ID del mozo")
                print("2. Modificar nombre del mozo")
                print("3. Modificar teléfono del mozo")
                print("4. Modificar estado del mozo")
                print("5. Salir")
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= 5:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            if opcion == 1:
                nuevo_id = input("Ingrese el nuevo ID del mozo (4 dígitos): ")
                if len(nuevo_id) == 4 and nuevo_id.isdigit():
                    if nuevo_id in data_mozos["id_mozo"].astype(str).values:
                        print("Error, el ID ya está registrado")
                    else:
                        data_mozos.at[mozo_index, "id_mozo"] = nuevo_id
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"ID del mozo actualizado a {nuevo_id}.")
                else:
                    print("El ID debe ser de 4 dígitos numéricos.")
            elif opcion == 2:
                nuevo_nombre = input("Ingrese el nuevo nombre del mozo: ")
                contiene_numero = False
                for caracter in nuevo_nombre:
                    if caracter.isdigit():
                        contiene_numero = True
                        print("El nombre no debe tener números")
                        break
                if not contiene_numero:
                    data_mozos.at[mozo_index, "nombre"] = nuevo_nombre
                    data_mozos.to_excel("Mozos.xlsx", index=False)
                    print(f"Nombre del mozo actualizado a {nuevo_nombre}.")
            elif opcion == 3:
                nuevo_telefono = input("Ingrese el nuevo teléfono del mozo (9 dígitos): ")
                if len(nuevo_telefono) == 9 and nuevo_telefono.isdigit():
                    if nuevo_telefono in data_mozos["telefono"].astype(str).values:
                        print("Error, el teléfono ya está registrado")
                    else:
                        data_mozos.at[mozo_index, "telefono"] = nuevo_telefono
                        data_mozos.to_excel("Mozos.xlsx", index=False)
                        print(f"Teléfono del mozo actualizado a {nuevo_telefono}.")
                else:
                    print("El teléfono debe ser de 9 dígitos numéricos.")
            elif opcion == 4:
                nuevo_estado = input("Ingrese el nuevo estado del mozo (Activo/Inactivo): ").title()
                if nuevo_estado in ["Activo", "Inactivo"]:
                    data_mozos.at[mozo_index, "estado"] = nuevo_estado
                    data_mozos.to_excel("Mozos.xlsx", index=False)
                    print(f"Estado del mozo actualizado a {nuevo_estado}.")
                else:
                    print("El estado debe ser 'Activo' o 'Inactivo'.")
            elif opcion == 5:
                print("Saliendo del menú de actualización de datos.")
                break
            
class Clientes:
    def __init__(self, id_Cliente=0, num_mesa=None, num_mozo=None, pedido=None, fecha=str, entregado=str):
        self.__id_Cliente = id_Cliente
        self.__num_mesa = num_mesa
        self.__num_mozo = num_mozo
        self.__pedido = []
        self.__fecha = fecha
        self.__entregado = entregado
        #self.agregar_pedido(pedido)
        
    @property
    def id_Cliente (self):
        return self.__id_Cliente
    
    @property
    def num_mesa (self):
        return self.__num_mesa
    
    @num_mesa.setter
    def num_mesa (self, num_mesa):
        self.__num_mesa = num_mesa
        
    @property
    def num_mozo (self):
        return self.__num_mozo
    
    @num_mozo.setter
    def num_mozo (self, num_mozo):
        self.__num_mozo = num_mozo
        
    @property
    def fecha (self):
        return self.__fecha
    @fecha.setter
    def fecha(self):
        return self.__fecha
    
    @property
    def entregado (self):
        return self.__entregado
    
    def agregar_pedido(self, pedido):
        pass
    
    def mostrar_clientes(self):
        df_clientes = pd.read_excel("Clientes.xlsx")
        print(tabulate(df_clientes, headers = "keys" , tablefmt = "grid"))
    
  
                    
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
    clientes = Clientes()
    restaurante = Restaurante(mozos,mesas)
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
                print("5. Eliminar mozos")
                print("6. Eliminar mesas")
                print("7. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if 1 <= subopcion <= 7:
                        if subopcion == 1:   
                            restaurante.registrar_mesas()
                        elif subopcion == 2:
                            restaurante.registrar_mozos()
                        elif subopcion == 3:
                            restaurante.reporte_registros()
                        elif subopcion == 4:
                            restaurante.reporte_mozos()
                        elif subopcion == 5:
                            mozos.eliminar_mozo()
                        elif subopcion == 6:
                            mesas.eliminar_mesa()
                        elif subopcion == 7:
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
                print("4. Modificar datos del mozo")
                print("5. Salir")
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                       mozos.asignar_mozo()
                    elif subopcion == 2:
                        mozos.cambiar_mozo()
                    elif subopcion == 3:
                        mesas.liberar_mesas()
                    elif subopcion == 4:
                        mozos.modificar_datos()
                    elif subopcion == 5:
                        print("Saliendo del menú de mozos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción invalida. Intente nuevamente.")
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
                    
        elif opcion == 3:
            while True:
                print("----------------------------------------")
                print("1. Registrar cliente")
                print("2. Realizar el pedido")
                print("3. Reporte de cuantos clientes tienen su pedido")
                print("4. Salir")   
                try:
                    subopcion = int(input("Seleccione una opcion: "))
                    if subopcion == 1:
                        restaurante.registrar_cliente()
                    elif subopcion == 2:
                        pass
                    elif subopcion == 3:
                        restaurante.reportes_clientes()
                    elif subopcion == 4:
                        print("Saliendo del menú de Clientes.")
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
                    elif subopcion == 3:
                        clientes.mostrar_clientes()
                        
                except ValueError:
                    print("Entrada invalida. Por favor, ingrese un numero.")
        else:
            print("Opcion no valida. Por favor, intente nuevamente.")
main()