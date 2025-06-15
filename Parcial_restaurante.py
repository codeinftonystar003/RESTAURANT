
from tabulate import tabulate
from datetime import datetime
# lista de mesas y mozos
#---------------------Antony----------------------------------
listaMesas= []
listaMozos= []
#---------------------Alexis----------------------------------
#lista general
listaClientes = []
#Listas dentro de los clientes
listaPlatos = []
listaPostre = []
listaBebidas = []
listaHPedidos = []
listaHMaxima = []
listaHEntrega = []
# ----------------------Lucero-----------------------------------
datosPagoMesa = []
listaPagos = []
pagosFinales = []
#----------------(caratula))---------------------------------------
def caratula():
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ".center(80))
    print("  @@@@@@@@@@@@@@@@@@@@@@@@@@@@  ".center(80))
    print("  @@   @@   @@    @@   @@   @@  ".center(80))
    print(" @@    @@   @@    @@   @@    @@ ".center(80))
    print("@@@   @@    @@    @@    @@   @@@".center(80))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@".center(80))
    print("@@   @@@    @@    @@    @@@   @@".center(80))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@".center(80))
    print(" @@@@@@@@@@@@@ @@  @@@@@@   @@@ ".center(80))
    print(" @@@@@@@@@@@@@@  @@@@@@@@@@  @@ ".center(80))
    print(" @@@@       @@@  @@@@@ @@@@  @@ ".center(80))
    print(" @@@@       @@@  @@@@@@@@@@  @@ ".center(80))
    print(" @@@@      @@@@    @@@@@@@   @@ ".center(80))
    print(" @@@@      @@@@@@@@@@@@@@@@@@@@ ".center(80))
    print(" @@@@       @@@@@@@@@@@@@@@@@@@ ".center(80))
    print(" @@@@       @@@              @@ ".center(80))
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ".center(80))
    print("================================".center(80))
    print("SISTEMA DE GESTIÓN DE PEDIDOS PARA RESTAURANTES".center(80))
    print("TRABAJO PARCIAL".center(80))
    print("================================".center(80))
    print("Curso: PROGRAMACIÓN ORIENTADO A OBJETOS".center(80))
    print("Docente: Juan Alfonso Ramírez Espinoza".center(80))
    print("2025-1".center(80))
    print("--------------------------------".center(80))
    print("Integrantes:".center(80))
    print("Hidalgo Martel, Joseph Edward (U202421665)".center(80))
    print("Huamán Flores, Alexis Miguel (U20241G114)".center(80))
    print("Peña Roña, Antony Jomar (U202421102)".center(80))
    print("Villavicencio Dávila, Ivette Lucero (U20241G010)".center(80))
    print("================================".center(80))
    print("================================".center(80))
    
def menu():
    print("--" * 30)
    print("<< MENU PRINCIPAL >>".center(60))
    print("--" * 30)
    print("[1] Registrar mesa y mozo 🍽️") 
    print("[2] Solicitar mozo        👨")
    print("[3] Tomar pedido          🍔")
    print("[4] Calcular pago         💵")
    print("[5] Ver reportes          📈")
    print("[6] Salir  ")
    print("--" * 30)
    print("<< ...SISTEMA RESTAURANTE -- BIENVENIDOS ...>>".center(60))
    print("--" * 30)   

# --------------------------------------------------Antony Yomar Peña Roña -----------------------------------------------------

def guardarMesas(numeroMesa, zonaMesa, capacidadMesa, estadoMesa):
    mesas = { "numeroMesa": numeroMesa,
                "zonaMesa": zonaMesa,
                "capacidadMesa": capacidadMesa,
                "estadoMesa": estadoMesa}
    listaMesas.append(mesas)
    
def mostrarMesas():
    if not listaMesas:
        print("No hay mesas registradas")
    else:
        print("Mesas registradas:")
        print(tabulate(listaMesas, headers="keys", tablefmt="grid"))
        
def guardarMozos(idMozo, nombreMozo, telefonoMozo, estadoMozo, capacidadMozo):
    mozos = {   "idMozo": idMozo,
                "nombreMoso": nombreMozo,
                "telefonoMozo": telefonoMozo,
                "estadoMozo": estadoMozo,
                "capacidadMozo": capacidadMozo,
                "mesasAsignadas": [] 
                }
    listaMozos.append(mozos)
def mostrarMozos():
    if not listaMozos:
        print("No hay mozos registrados")
    else:
        print("Mozos registrados:")
        print(tabulate(listaMozos, headers="keys", tablefmt="grid"))       
def registrarMesa():
    print("Registro de mesas".center(80, "-"))
    print("-" * 80)
    while True:
        existeMesa = False
        numeroMesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
        if 1<= numeroMesa <= 100:
            for  id  in listaMesas:
                if id["numeroMesa"] == numeroMesa:
                    existeMesa = True
                    break
            
        if  not existeMesa and 1<= numeroMesa <= 100:
            break
        else:
            print("Error, el numero de mesa no esta en rango o ya existe")
    
    while True:
        zonaMesa = input("Ingrese la zona de disponibilidad de la mesa (sala/terraza): ").lower()
        if zonaMesa in ["sala","terraza"]:
            break
        else:
            print("Error, la zona no es correcta")
            
    while True:
        try:
            capacidadMesa = int(input("Ingrese la capacidad de la mesa (1 - 4): "))
            if 1<= capacidadMesa <= 4:
                break
            else:
                print("Error, la capacidad de la mesa no es correcta")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estadoMesa = input("Ingrese el estado de la mesa (libre/ocupada/reservada): ").lower()
        if estadoMesa in ["libre","ocupada","reservada"]:
            break
        else:
            print("Error, el estado de la mesa no es correcto")
    print("-" * 80)
    print("Mesa registrada correctamente".center(80))
    print("-" * 80)
    guardarMesas (numeroMesa, zonaMesa, capacidadMesa, estadoMesa)
    
def registrarMozos():
    print("-" * 80)
    print("Registro de mozos".center(80, "-"))
    print("-" * 80)
    
    while True:
        existeMozo = False
        idMozo = input("Ingrese el id del mozo (4 digitos): ")
        if len(idMozo) == 4 and idMozo.isdigit():
            for id in listaMozos:
                if id["idMozo"] == idMozo:
                    existeMozo = True
                    break
            if not existeMozo:
                break
            else:
                print("Error, el id del mozo ya existe")
        else:
            print("Error en los datos de ingreso")
            
            
    while True:
        nombreMoso = input("Ingrese el nombre y apellido del mozo: ")
        contieneNumero = False 
        for caracter in nombreMoso:
            if caracter.isdigit():
                contieneNumero = True
                print("El nombre no debe tener numeros")
                break
            
        if not contieneNumero:
            break

    while True:
        telefono = False
        try:
            telefonoMozo = input("Ingrese el telefono del mozo (9 digitos): ")
            if len(str(telefonoMozo)) == 9:
                for cell in listaMozos:
                    if id["telefonoMozo"] == telefonoMozo:
                        telefono = True
                        break
                if not telefono:
                    break
                else:
                    print("El telefono del mozo ya existe")
            else:
                print("Error, el telefono del mozo no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
    
    while True:
        estadoMozo = input("Ingrese el estado del mozo (activo/inactivo) sin espacios: ").lower()
        if estadoMozo in ["activo","inactivo"]:
            break
        else:
            print("Error, el estado del mozo no es correcto")
            
    capacidadMozo = 4
    guardarMozos(idMozo, nombreMoso, telefonoMozo, estadoMozo, capacidadMozo)
    print("-" * 80)
    print("Mozo registrado correctamente".center(80))
    print("-" * 80)
def asignarMozos():
    mostrarMozos()
    if not listaMozos:
        print("No hay mozos registrados")
        return
    while True:
        idMozo = input("Ingrese el id del mozo a asignar (4 digitos): ")
        if len(idMozo) == 4 and idMozo.isdigit():
            break
        else:
            print("Error, el id del mozo no es correcto")
            
    mozoSelec = None
    for id in listaMozos:
        if id["idMozo"] == idMozo :
            if id["estadoMozo"] == "activo":
                mozoSelec = id
                break
            else:
                print("Error, el mozo no esta disponible")
                return
    else:
        print("Error, el id del mozo no esta registrado")
        return
    
    if len(mozoSelec["mesasAsignadas"]) >= 4:
        print("-" * 80)
        print("Error, el mozo no puede atender más mesas".center(80))
        print("-" * 80)
        return
    
    while True:
        try:
            numeroMesa = int(input("Ingrese el numero de mesa a reservar (1 - 100) sin espacios: "))
            if 1<= numeroMesa <= 100:
                break
            else:
                print("Error, el numero de mesa no es correcto")
        except ValueError:
            print("Error en los datos de ingreso")
    
            
    for id in listaMesas:
        if id["numeroMesa"] == numeroMesa:
            mesas_asignadas = id["numeroMesa"]
            if mesas_asignadas not in mozoSelec["mesasAsignadas"]:
                if id["estadoMesa"] == "libre":
                    confirmarPedido = input("¿Desea confirmar la reserva? (si/no): ").lower()
                    if confirmarPedido == "si":
                        id["estadoMesa"] = "reservada"
                        print("-" * 80)
                        print("Mesa reservada correctamente".center(80))
                        print("-" * 80)
                        mozoSelec["mesasAsignadas"].append(numeroMesa)
                        
                           # Cambiar estado del mozo a "inactivo" si tiene 4 mesas asignadas
                        if len(mozoSelec["mesasAsignadas"]) == 4:
                            mozoSelec["estadoMozo"] = "inactivo"
                            print("-" * 80)
                            print(f"El mozo {mozoSelec['nombreMoso']} ahora está inactivo.".center(80))
                            print("-" * 80)
                        break    
                    elif confirmarPedido == "no":
                        print("Reserva cancelada")
                        break
                    else:
                        print("Error, la opción no es correcta")
                else:
                    print("Error, la mesa no esta disponible")
                    break
            else:
                print("Error, la mesa ya está asignada")
                break
    else:
        print("La mesa no esta registrada")
def Cambiar_mozo():
    mostrarMozos()
    if not listaMozos:
        print("No hay mozos registrados")
        return

    while True:
        idMozo = input("Ingrese el id del mozo a cambiar (4 dígitos): ")
        idNuevoMozo = input("Ingrese el id del nuevo mozo (4 dígitos): ")
        if len(idMozo) == 4 and idMozo.isdigit() and len(idNuevoMozo) == 4 and idNuevoMozo.isdigit():
            break
        else:
            print("Error, ambos IDs deben ser numéricos de 4 dígitos")

    while True:
        try:
            numeroMesa = int(input("Ingrese el número de mesa a cambiar mozo (1 - 100): "))
            if 1 <= numeroMesa <= 100:
                break
            else:
                print("Error, el número de mesa debe estar entre 1 y 100")
        except ValueError:
            print("Error en el número de mesa")
            return

    # Buscar el nuevo mozo
    nuevoMozo = None
    for mozo in listaMozos:
        if mozo["idMozo"] == idNuevoMozo:
            if mozo["estadoMozo"] == "activo":
                nuevoMozo = mozo
                break
            else:
                print("Error, el nuevo mozo no está disponible")
                return
    if nuevoMozo is None:
        print("Error, el ID del nuevo mozo no está registrado")
        return

    # Buscar el mozo actual y quitar la mesa
    mozoActual = None
    for mozo in listaMozos:
        if mozo["idMozo"] == idMozo:
            mozoActual = mozo
            if numeroMesa in mozo["mesasAsignadas"]:
                mozo["mesasAsignadas"].remove(numeroMesa)
                if len(mozo["mesasAsignadas"]) < 4:
                    mozo["estadoMozo"] = "activo"
                break
            else:
                print("Error, la mesa no está asignada al mozo actual")
                return
    if mozoActual is None:
        print("Error, el mozo actual no se encuentra registrado")
        return

    # Asignar la mesa al nuevo mozo
    if len(nuevoMozo["mesasAsignadas"]) < 4:
        nuevoMozo["mesasAsignadas"].append(numeroMesa)
        print("-" * 80)
        print("Cambio de mozo realizado correctamente".center(80))
        print("-" * 80)
    else:
        print("Error, el nuevo mozo no puede atender más mesas")  
# ------------------------------------------Alexis Huaman------------------------------------------------------------------
# (Registro de pedidos)
def cartas():
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Salir]")
        
def cartaPlatos():
    platos = {
        1: ["Lomo Saltado", 35.00],
        2: ["Ceviche", 35.00],
        3: ["Causa limeña", 25.00],
        4: ["Arroz con pollo", 20.00],
        5: ["Aji de gallina", 20.00],
        6: ["Pollo a la brasa", 24.00],
        7: ["Papa Rellena", 25.00],
        8: ["Chicharron de pescado", 30.00],
        9: ["Tallarines verdes", 25.00],
        10: ["Tallarines Rojos", 25.00]
        }
    print("--" * 30)
    print("<< MENU DE PLATILLOS DE FONDO >>".center(60))
    print("--" * 30)
    print("Platillos:", " "*28, "Precio:")
    for i, (nombrePrecios) in enumerate(platos.values(), start=1):
        print(f"{i}. {nombrePrecios[0]:<40} s/. {nombrePrecios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return platos

def cartaPostres():
    postres= {
        1: ["Mazamorra morada", 12.00],
        2: ["Arroz con leche", 12.00],
        3: ["Suspiro a la limeña", 10.00],
        4: ["Picarones", 15.00],
        5: ["Alfajores", 10.00],
        6: ["Torta de chocolates", 18.00],
        7: ["Turron", 15.00],
        8: ["King kong de manjar blanco",12.00]
    }
    
    print("--" * 30)
    print("<< MENU DE POSTRES >>".center(60))
    print("Postres:", " "*30, "Precios:")
    for num, nombrePrecios in enumerate(postres.values(),start=1):
        print (f"{num}.{nombrePrecios[0]:<40} s/. {nombrePrecios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return postres

def cartaBebidas():
    bebidas = {
        1: ["Chicha morada", 18.00],
        2: ["Chicha de jora", 18.00],
        3: ["CocaCola", 10.00],
        4: ["InkaCola", 10.00],
        5: ["Jugo natural", 10.00],
        6: ["Cafe", 6.00],
        7: ["Pisco Sour", 20.00],
        8: ["Chilcano de pisco", 18.00]
    }
    print("--" * 30)
    print("<< MENU DE BEBIDAS >>".center(60))
    print("--" * 30)
    print("Bebidas:", " "*30, "Precio:")
    for num, nombrePrecios in enumerate(bebidas.values(), start=1):
        print(f"{num}.{nombrePrecios[0]:<40} s/. {nombrePrecios[1]}")
    print("[0. Regresar]  ")
    print("--" * 30)
    return bebidas

def guardarCliente(numeroMesa, mozoAsignado, listaPlatos, listaPostre, listaBebidas, listaHPedidos, listaHMaxima, listaHEntrega): 
    cliente = {
        "numeroMesa": numeroMesa,
        "nMozo" : mozoAsignado,
        "plato" : listaPlatos.copy(),
        "postre" : listaPostre.copy(),
        "bebida" : listaBebidas.copy(),
        "hPedido" : listaHPedidos.copy(),
        "hMaxima" : listaHMaxima.copy(),
        "hEntrega" : listaHEntrega.copy()
    }
    listaClientes.append(cliente)
    
def mostrarCliente():
    if not listaClientes:
        print("La lista esta vacia")
    else:
        print("El mozo asignado es: ", listaClientes[0]["nMozo"])
        print(tabulate(listaClientes,headers="keys",tablefmt="grid"))    
           
def registrarPedido():
    
    while True:
        try:
            existeMesa = False
            numeroMesa = int(input("Ingrese el numero de  mesa a registrar (1 - 100): "))
            if 1<= numeroMesa <= 100:
                for  id  in listaMesas:
                    if id["numeroMesa"] == numeroMesa:
                        existeMesa = True
                        break
            if existeMesa:
                break
            else:
                print("Error, el numero de mesa no es correcto") 
        except ValueError:
            print("Valor incorrecto")
    
    while True:
        print("--" * 30)
        print("<< BIENVENIDO AL MENU >>".center(60))
        print("Seleccionar que desea: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("4. Registrar hora de pedido (Necesario)")
        print("5. Registrar hora de entrega")
        print("[0. Salir]")
        opcion = int(input ("Ingresar opcion: "))
        
        if opcion == 1:
            platos = cartaPlatos()
            while True:
                opcion = int(input("Elegir opcion de plato: "))
                if 1<= opcion <= 10:
                    plato = platos[opcion] # platos[opcion] = nombre, precio
                    listaPlatos.append(plato)
                    break
                else:
                    print("No existe opcion.")
                    
        elif opcion == 2:
            postres = cartaPostres()
            while True:
                opcion = int(input("Elegir opcion del postre: "))
                if 1<= opcion <= 8:
                    postre = postres[opcion] # 
                    listaPostre.append(postre)
                    break
                else:
                    print("No existe opcion.")
        elif opcion == 3:
            bebidas = cartaBebidas()
            while True:
                opcion = int(input("Elegir opcion de bebida: "))
                if 1<= opcion <= 10:
                    bebida = bebidas[opcion]
                    listaBebidas.append(bebida)
                    break
                
        elif opcion == 4:
            fechaPedido = datetime.now()
            hPedido = fechaPedido.hour
            mPedido = fechaPedido.minute
            print("--" * 30)
            print("--" * 30)
            print("<< HORA DE PEDIDO >>".center(60))
            print(f"Hora de pedido:  {hPedido} horas con {mPedido} minutos.")
            if mPedido + 30 >= 60:
                mMaximo = (mPedido + 30) - 60
                hMaxima = hPedido + 1      
                if hMaxima > 24:
                    hMaxima = (hPedido + 1) - 24
            else:
                
                hMaxima = hPedido
                mMaximo = mPedido + 30
            print("<< HORA DE MAXIMA DE ENTREGA >>".center(60))
            print(f"Hora maxima de entrega: {hMaxima} horas con {mMaximo} minutos.")
            print("--" * 30)
            print("--" * 30)
            listaHPedidos.append((hPedido, mPedido))
            listaHMaxima.append((hMaxima, mMaximo))
            break
        elif opcion == 5:
            try:
                print("-"* 30)
                print("Ingresar la hora de entrega de su pedido (en formato 24h): ")
                hEntrega = int(input("Ingresar hora: "))
                mEntrega = int(input("Ingresar minuto: "))
                if hEntrega >= 0 and hEntrega <= 24 and mEntrega >= 0 and mEntrega < 60:
                    for cliente in listaClientes:
                        if cliente["numeroMesa"] == numeroMesa:
                            if cliente["hPedido"]:
                                hPedido, mPedido = cliente["hPedido"][-1]
                                tPedido = hPedido * 60 + mPedido
                                tEntrega = hEntrega * 60 + mEntrega
                                if tEntrega > tPedido and tEntrega <= 1440:
                                    print("-" * 30)
                                    print("<< HORA DE ENTREGA REGISTRADO CORRECTAMENTE >>".center(80))
                                    print("-" * 30)
                                    cliente["hEntrega"].append((hEntrega, mEntrega))
                                else:
                                    print("-" * 30)
                                    print("La hora de entrega debe ser mayor a la hora del pedido")
                                    print("-" * 30)
                            else:
                                print("-" * 30)
                                print("No hay una hora de pedido registrada")
                                print("-" * 30)
                            break
                    else:
                        print("-" * 30)
                        print("No hay un cliente registrado para esta mes")
                        print("-" * 30)
                else:
                    print("-" * 30)
                    print("Error con la hora introducida")
                    print("-" * 30)
            except ValueError:
                print("-" * 30)
                print("Valor incorrecto")
                print("-" * 30)
        elif opcion == 0:
            print("-" * 30)
            print("Regresando...")
            break
        else:
            print("Opcion no existente")
                
    for mozo in listaMozos:
        if numeroMesa in mozo["mesasAsignadas"]:
            mozoAsignado = mozo["nombreMoso"]
        
    if listaPlatos or listaPostre or listaBebidas or listaHPedidos or listaHMaxima or listaHEntrega:
        guardarCliente(numeroMesa, mozoAsignado, listaPlatos, listaPostre, listaBebidas, listaHPedidos, listaHMaxima, listaHEntrega)
        
    listaPlatos.clear()
    listaPostre.clear()
    listaBebidas.clear()
    listaHPedidos.clear()
    listaHMaxima.clear()
    listaHEntrega.clear() 
    
# (ELIMINAR PEDIDOS)
def eliminarPedido(): 
    while True:
        print("--" * 30)
        print("<< ELIMINAR PEDIDOS >>".center(60))
        print("--" * 30)
        existeMesa = False
        existeCliente = False
        mesa = int(input("Ingrese el numero de mesa del cliente (si no desea precione 0): "))
        if mesa == 0:
            break
        if 1 <= mesa <= 100: 
            existeMesa = True
            for cliente in listaClientes:
                if mesa == cliente['numeroMesa']:
                    existeCliente = True
                    break 
        if not existeMesa:
            print("Error, el numero de mesa no es correcto")
            continue
        if not existeCliente:
            print("Error, no hay un cliente registrado")
            continue
        print("-"* 30)
        print("Que es lo que desea eliminar: ")
        print("1. Platos")
        print("2. Postres")
        print("3. Bebidas")
        print("[0. Regresar]")
        elim = int(input("Ingrese la opcion: "))
        if elim == 1:
            if cliente["plato"] != []:
                print("Platos:")
                for i, pedido in enumerate(cliente["plato"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero del plato a eliminar (Salir = 0): "))
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["plato"]):
                        cliente["plato"].pop(eliminar-1)
                        print("Plato eliminado correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de plato no es correcto")
            else:
                print("No hay platos registrados para eliminar")
        elif elim == 2:
            if cliente["postre"] != []:
                print("Postres:")
                for i, pedido in enumerate(cliente["postre"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero del postre a eliminar (Salir = 0): "))
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["postre"]):
                        cliente["postre"].pop(eliminar-1)
                        print("Postre eliminado correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de postre no es correcto")
            else:
                print("No hay postres registrados para eliminar")
        elif elim == 3:
            if cliente["bebida"] != []:
                print("Bebidas:")
                for i, pedido in enumerate(cliente["bebida"], start=1):
                    print(f"{i}. {pedido[0]} con precio: {pedido[1]}")
                while True:
                    eliminar = int(input("Ingrese el numero de la bebida a eliminar (Salir = 0): "))
                    print("Si no desea eliminar presione 0")
                    if eliminar == 0:
                        print("Regresando...")
                        break
                    if 1 <= eliminar <= len(cliente["bebida"]):
                        cliente["bebida"].pop(eliminar-1)
                        print("Bebida eliminada correctamente".center(80))
                        print("-" * 80)
                    else:
                        print("Error, el numero de bebida no es correcto")
            else:
                print("No hay bebidas registradas para eliminar")
        elif elim == 0:
            break
        else:
            print("Opcion incorrecta") 
                  
#------------------------------------------------------------------- Lucero -------------------------------------------------------------------------- 
def pagoFinal():
    print("-"*50)
    print("<< CALCULO >>".center (61))
    print("-"*50)
    pagoFinal = 0
   
    while True:
        try:
            existeMesa = False
            numeroMesa=int(input("Digite el numero de mesa a pagar : "))
            if 1<= numeroMesa <= 100:
                for mesa in listaMesas:
                    if mesa["numeroMesa"] == numeroMesa:
                        existeMesa = True
                        break
                if not existeMesa:
                    print("El numero de mesa no esta registrado")
                else:
                    break
            else:
                print("El numero de mesa esta fuera de rango")
        except ValueError:
            print("Valor incorreto.")


    for clientes in listaClientes: 
        if numeroMesa == clientes["numeroMesa"]: #encontrar el numero de mesa ingresado en la lista de clientes 
            #----------------------- hallar el precio de cada consumo de la mesa
            if listaPlatos or listaPostre or listaBebidas:
                pagoPlato = int(clientes["plato"][0][1])
                pagoPostre= int(clientes["postre"][0][1])
                pagoBebida= int(clientes["bebida"][0][1])
                pagoFinal= pagoPlato + pagoPostre + pagoBebida
    #----------------------- convertir a minutos la hr de pedido
                auxiliar1 = clientes["hPedido"]
                auxiliar2 = clientes["hPedido"]
                horaPedido = auxiliar1[0][0]
                minutoPedido = auxiliar2[0][1]
                totalMinPedido = horaPedido*60 + minutoPedido                         
                #----------------------- convertir a minutos la hr de entrega
                hEntrega_H= clientes["hEntrega"][0][0]
                hEntrega_M= clientes["hEntrega"][0][1]
                convertir_min_entrega = hEntrega_H*60 + hEntrega_M        
        #----------------------- convertir a minutos la hr de entrega
                hEntrega_H= clientes["hEntrega"][0][0]
                hEntrega_M= clientes["hEntrega"][0][1]
                convertir_min_entrega = hEntrega_H*60 + hEntrega_M
            
    # si el tiempo de entrega paso el limite de 30 min de espera
        if convertir_min_entrega > totalMinPedido+30: 
            print ( "--" *30)
            print(" ‼Debido a que el tiempo de espera fue mas de 30 minutos...")
            print("---> ¡Ud. ha recibido un DESCUENTO AUTOMATICO del 10% del pago total!")
            print("--"*30)
            descuento= pagoFinal * 0.10
            pagoFinal=pagoFinal- descuento
            print(f"\nEl pago total por la mesa #{numeroMesa} es {pagoFinal} soles.")
        else:
            print(f"\nEl pago total por la mesa #{numeroMesa} es {pagoFinal} soles.")
        
        propina= input("Sugerimos propina del 10% sobre el pago total, desea aceptar (si/no) ?: ")
        if propina.lower()=="si":
            propinaTotal = pagoFinal * 0.10
            pagoFinal= pagoFinal + propinaTotal 
            
        elif propina.lower()=="no":
            print("...esta bien, no se preocupe!")
        else:
            print("El formato de  respueta no es correcto")
        
        pagoFinal = [clientes["numeroMesa"], pagoFinal]
            
    pagosFinales.append(pagoFinal)
    print("=" * 60)
    print(f"{'Resumen de Pago':^60}")
    print("-" * 60)
    print(f"{'Mesa #:':<20} {numeroMesa}")
    print(f"{'Total a pagar:':<20} {pagosFinales[0][1]} soles")
    print("-" * 60)
    print(f"{'¡Gracias por su visita!':^60}")
    print("=" * 60)
    pagoFinal.clear()
            

def pagoxMesa():
    pagoFinal = pagosFinales[0]
    for pagoxMesa in pagosFinales:
        for mesa, pago in pagoFinal.items():
            datosPagoMesa.append([mesa,pago])
    
    print("<< TABLA DE PAGO POR MESA >>".center(60))
    columnas=["MESA", "PAGO S/."]
    print(tabulate(datosPagoMesa, headers = columnas, tablefmt="grid"))
# ------------------------------------------- JOSEPH  ------------------------------------------------------------------------------------------
def mozoMasPedido():
    if not listaClientes or not listaMozos:
        print("No hay mozos registrados o no hay pedidos registrados")
        return

    mozos_items = {}
    for mozo in listaMozos:
        mozos_items[mozo['nombreMoso']] = 0
    
    for cliente in  listaClientes:
        mozo = cliente['nMozo']
        if mozo in mozos_items:
            mozos_items[mozo] += len(cliente['plato'])
            mozos_items[mozo] += len(cliente['postre'])
            mozos_items[mozo] += len(cliente['bebida'])
    
    if not mozos_items or sum(mozos_items.values()) == 0:
        print("No hay pedidos registrados")
        return

    mozo_top = ("", 0)
    for nombre, cantidad in mozos_items.items():
        if cantidad > mozo_top[1]:
            mozo_top = (nombre, cantidad)
    
    items_list = []
    for nombre, cantidad in mozos_items.items():
        items_list.append((cantidad, nombre))
    
    tabla_datos = []
    for posicion, (cantidad, nombre) in enumerate(items_list, start=1):
        tabla_datos.append([posicion, nombre, cantidad])
    
    print("\n" + "="*60)
    print("MOZO CON MÁS PEDIDOS ATENDIDOS".center(60))
    print("="*60)
    print(tabulate(tabla_datos, headers=['Mozo', 'Total Pedidos'],tablefmt='grid'))
    print("="*60)
    print(f"¡El mozo más eficiente es {mozo_top[0]} con {mozo_top[1]} pedidos atendidos!".center(60))
    print("="*60 + "\n")   
def tiempoEspera():
    if not listaClientes:
        print("No hay pedidos registrados para calcular tiempos de espera")
        return
    
    total_pedidos = 0
    tiempo_total = 0  # en minutos
    pedidos_tardios = 0
    
    print("\n" + "="*60)
    print("TIEMPO DE ESPERA POR PEDIDO".center(60))
    print("="*60)
    
    imprimir_promedio = []
    
    for cliente in  listaClientes:
        if not cliente['hPedido'] or not cliente['hEntrega']:
            continue
            
        # Obtener tiempos
        hPedido, mPedido = cliente['hPedido'][0]
        hEntrega, mEntrega = cliente['hEntrega'][0]
        hMaxima, minuto_maximo = cliente['hMaxima'][0]
        
        # Calcular tiempo en minutos
        tPedido = hPedido * 60 + mPedido
        tEntrega = hEntrega * 60 + mEntrega
        tiempo_maximo = hMaxima * 60 + minuto_maximo
        
        # Calcular tiempo de espera
        tiempo_espera = tEntrega - tPedido
        
        # Verificar si fue tardío
        tardio = "Sí" if tEntrega > tiempo_maximo else "No"
        if tardio == "Sí":
            pedidos_tardios += 1
            
        # Acumular para promedio
        total_pedidos += 1
        tiempo_total += tiempo_espera
        
        # Agregar a tabla
        imprimir_promedio.append([
            cliente['numeroMesa'],
            f"{hPedido:02d}:{mPedido:02d}",
            f"{hEntrega:02d}:{mEntrega:02d}",
            f"{tiempo_espera} min",
            tardio
        ])
    
    if total_pedidos == 0:
        print("No hay pedidos completos con hora de entrega registrada")
        return
    
    promedio_espera = tiempo_total / total_pedidos
    porcentaje_tardios = (pedidos_tardios / total_pedidos) * 100
    
    print(tabulate(imprimir_promedio, 
                  headers=['Mesa', 'Hora Pedido', 'Hora Entrega', 'Tiempo Espera', 'Tardío'],
                  tablefmt='grid'))
    
    print("\n" + "ESTADÍSTICAS GENERALES".center(60))
    print(f"Tiempo promedio de espera: {promedio_espera:.1f} minutos")
    print(f"Pedidos entregados a tiempo: {100 - porcentaje_tardios:.1f}%")
    print(f"Pedidos entregados tarde: {porcentaje_tardios:.1f}%")
    print("="*60 + "\n")
def mayorConsumo():
    
    imprimir=[]
    if not datosPagoMesa:
        print("No hay suficientes datos para generar este reporte")
        return
    mesa_mayor = 0
    consumo_mayor = 0
    
    for pago in datosPagoMesa:
        mesa, consumo = pago
        if consumo > consumo_mayor:
            consumo_mayor = consumo
            mesa_mayor = mesa
    imprimir.append([mesa_mayor,f"S/. {consumo_mayor}"])
    
    print("\n" + "="*60)
    print("MESA CON MAYOR CONSUMO (VENTAS TOTALES POR MESA)".center(60))
    print("="*60)
    print(tabulate(imprimir, headers=["Mesa", "Consumo Total"], tablefmt="grid"))
    print("\n" + "RESULTADO:".center(60))   
def ingresosZona():
    if not datosPagoMesa:
        print("No hay suficiente datos para generar el reporte")
        return
    ingresos_sala=0
    ingresos_terraza=0
    mesas_sala=0
    mesas_terraza=0
    mesa_zona={}
    for mesa in listaMesas():
        mesa_zona[mesa["numeroMesa"]] = mesa["zonaMesa"]
    
    for mesa,consumo in datosPagoMesa.items():
        if mesa in mesa_zona:
            zona=mesa_zona[mesa]
            if zona=="sala":
                ingresos_sala+=consumo
                mesas_sala+=1
            elif zona=="terraza":
                ingresos_terraza+=consumo
                mesas_terraza+=1
    total_ingreso=ingresos_sala+ingresos_terraza
    total_mesas=mesas_sala+mesas_terraza
    porcentaje_sala=(ingresos_sala/total_ingreso)*100
    porcentaje_terraza=(ingresos_terraza/total_ingreso)*100
    imprimir=[[f"Sala",f"S/.{ingresos_sala}",mesas_sala],[f"Terraza",f"S/.{ingresos_terraza}"],["Total",f"S/.{total_ingreso}",total_mesas]]
    print("\n" + "═"*60)
    print(" INGRESOS POR ZONA (SALA VS. TERRAZA) ".center(60))
    print("═"*60)
    print(tabulate(imprimir,headers=["Zona", "Ingresos Totales", "Mesas Atendidas"],tablefmt="grid"))
    print("\n" + "ANÁLISIS DE DEMANDA:".center(50))
    print(f"- Sala: {porcentaje_sala:.1f}% de los ingresos")
    print(f"- Terraza: {porcentaje_terraza:.1f}% de los ingresos")
#-------------------------------------------- MAIN ---------------------------------------------------------------------------------------------       
def main():
    #caratula() 
    while True:
        menu()
        while True:
            try:
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= 7:
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")   
        if opcion == 1:
            while True:
                print("----------------------------------------")
                print("1. Registrar mesas")
                print("2. Registrar mozos")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if 1 <= subopcion <= 3:
                        if subopcion == 1:   
                            registrarMesa() # 1. Registrar mesas
                        elif subopcion == 2:
                            registrarMozos() # 2. Registrar mozos
                        elif subopcion == 3:
                            break
                        else:
                            print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                
        elif opcion == 2:  # Asignar mozo a mesa
            while True:
                print("----------------------------------------")
                print("1. Asignar mozo a mesa")
                print("2. Cambiar mozo de la mesa actual")
                print("3. Salir")
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if subopcion == 1:
                        asignarMozos()
                    elif subopcion == 2:
                        Cambiar_mozo()
                    elif subopcion == 3:
                        print("Saliendo del menú de mozos.")
                        break  # Salimos del bucle porque eligió salir
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == 3: # Reaizar el pedido 
            while True:
                print("----------------------------------------")
                print("1. Añadir pedido y ver datos del pedido")
                print("2. Eliminar items")
                print("[0. Regresar]")
                try:
                    opcion = int(input ("Ingresar opcion: "))
                    if  opcion == 1:
                        registrarPedido()
                    elif opcion == 2:
                        eliminarPedido()
                    elif opcion == 0:
                        break
                except ValueError:
                    print("Valor incorrecto")
                    
        elif opcion == 4:
              while True: 
                print("----------------------------------------")
                print("1. Pago final por mesa")
                print("2. Mostrar reporte de pago por mesa")
                print("3. Salir")
                try:
                    opcion=int(input("Digite la opcion: "))
                    if opcion== 1:
                        pagoFinal()
                    elif opcion==2:
                        pagoxMesa()
                    elif opcion==3:
                        break
                except ValueError:
                    print("Error, digite un numero")
    
        elif opcion == 5: # Aqui se muestran los reportes de los mozos , mesas y los pedidos de los clientes
            while True:
                print("1. Mostrar mesas")
                print("2. Mostrar mozos")
                print("3. Mostrar pedidos clientes")
                print("4. Mostrar mozo con mas pedidos")
                print("5. Mostrar promedio tiempo espera")
                print("6. Mostrar mesa mayor consumo")
                print("7. Mostrar ingresos por zona (sala/Terrasa)")
                print("8. salir")
                try:
                    subopcion = int(input("Seleccione una opción: "))
                    if subopcion == 1:
                        mostrarMesas() # Mostrar mesas registradas
                    elif subopcion == 2:
                        mostrarMozos() # Mostrar mozos registrados
                    elif subopcion == 3:
                        mostrarCliente() # Mostrar los pedidos de los clientes
                    elif subopcion == 4:
                        mozoMasPedido()
                    elif subopcion == 5:
                        tiempoEspera()
                    elif subopcion == 6:
                        mayorConsumo()
                    elif subopcion == 7:
                        ingresosZona()
                    elif subopcion == 8:
                        break
                    else:
                        print("La opcion es incorrecta")
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
        
        elif opcion == 6:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
main()