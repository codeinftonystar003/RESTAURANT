import pandas as pd
mesas = pd.read_csv("Mesas.csv", sep = ",")
mozos = pd.read_csv("Mozos.csv", sep = ",")
# Eliminar espacios ocultos en los nombres de columnas
mozos.columns = mozos.columns.str.strip()
mesas.columns = mesas.columns.str.strip()
# print(mozos[mozos["estado"] ==  "Activo"])
"""
def encontrar_mozos():
    id = int(input("Ingrese un id del mozo a buscar: "))
    resultado = mozos[mozos["id_mozo"] == id]
    if not mozos.empty:
        print(resultado)
    else:
        print("EL MOZO NO SE ENCUENTRA")
    
    for fila, columna in resultado.iterrows():
        print(columna["telefono"])
        print(columna["estado"])
        
encontrar_mozos()
"""
def encontrar_mozo(id):
    resultado = mozos[mozos["id_mozo"] == id]
    if not  resultado.empty:
        return resultado
    else:
        return None
def encontrar_meza(numero):
    resultado = mesas[mesas["numero_mesa"] == numero]
    if not resultado.empty:
        return resultado
    else:
        return None
    
def agregar_meza ():
    while True:
        id = int(input("Ingrese el id del mozo a asignar: "))
        mozo = encontrar_mozo(id)
        if mozo is not None and mozo.iloc[0]["estado"] == "Activo":
            print("segir con el proceso")
            print(mozo)
            break
        else:
            print("El mozo no esta registrado")
    
    while True:
        numero_mesa = int(input("Ingrese el numero de mesa a asignar: "))
        mesa = encontrar_meza(numero_mesa)
        if mesa is not None and mesa.iloc[0]["estado_mesa"] == "Libre":
            asignadas = mozo.iloc[0]["mesas_reservadas"]
            if pd.isna(asignadas):
                lista = []
            else:
                if isinstance(asignadas, str):
                    lista = eval(asignadas)
                else:
                    lista = list(asignadas)

            if len(lista) >= 4:
                print("❌ Este mozo ya tiene 4 mesas asignadas. No se puede asignar más.")
                return
            
            lista.append(numero_mesa)
            print(f"✅ Mesa {numero_mesa} asignada al mozo {mozo.iloc[0]['nombre']}.")
            if len(lista) == 4:
                index_mozo = mozo.index[0]
                mozos.at[index_mozo, "estado"] = "Inactivo"
                print("⚠️ El mozo ha alcanzado el límite de 4 mesas. Ahora está inactivo.")

            # Actualizar el Dataframe de mozos
            index_mozo = mozo.index[0]
            mozos.at[index_mozo, "mesas_reservadas"] = str(lista)
            # Cambiar 
            index_mesa = mesa.index[0]
            mesas.at[index_mesa,"estado_mesa"] = "Reservada"
            
            # Guardar cambios en los archivos CSV
            mozos.to_csv("Mozos.csv", index=False)
            mesas.to_csv("Mesas.csv", index=False)
            break
        else:
            print("Error la mesa no existe o no esta disponible ")
            
    
agregar_meza()
