
# -------------------------------------------- #

#Listas Principales
productos = []
precios = []
indices = []
cart = []
subtotal = []


# Variables Globales
auxi1 = ""
auxi2 = ""
items = 0
salida = False
Sale_Final = True

# -------------------------------------------- #
# --- Funciones --- #

def agregar_producto():
        producto = str(input('Nombre del Producto: '))  # entrada producto
        global auxi1 
        auxi1 = producto
        return producto

def agregar_precio():
        precio = int(input('Precio del Producto: $ '))  # entrada precio
        global auxi2
        auxi2 = precio
        return precio
 
def addProducts():
    out = False
    while out == False:
        paquete = agregar_producto() # guardo producto
        productos.append(paquete)    # agrego a la lista
        indice1 = (productos.index(auxi1)) # guardo el indice para usar despues
        indices.append(indice1)
        
        monto = agregar_precio()        # guardo precio
        precios.append(monto)           # agrego precio
        #indice2 = (precios.index(auxi2))
        #print(indice2)

        print("<- Productos Agregados ->")
        print()
        print(f"Productos: {productos}")      
        print()    
        print("Agregar mas Productos? ")
        print()
        respuesta = str(input('Ingrese [ y =si / n =no ] : '))
        negativo = "n"
        if respuesta == negativo:
           out = True

def remove(lista, producto):
    item = str(producto)
    delete = (lista.index(item))
    lista.pop(delete)

def removeProducts():
    out = False
    while out == False:
        print()
        print(productos)
        print()
        print("<pulse 's' para volver>")
        print()
        respuesta = str(input('Ingrese el producto a eliminar : '))
        if respuesta == "s":
            out = True
        else:
            costo = productos.index(respuesta)
            precios.pop(costo)
            remove(productos, respuesta)
            print("Eliminar otro Producto? ")
            respuesta2 = str(input('Ingrese [ y =si / n =no ] : '))
            negativo = "n"
            if respuesta2 == negativo:
                out = True

def removeCart():
    out = False
    while out == False:
        print()
        print("<pulse 's' para volver>")
        print()
        print(cart)
        respuesta = str(input('Ingrese el producto a Eliminar: '))
        if respuesta == "s":
            out = True
        else:
            delete = cart.index(respuesta)
            cart.pop(delete)
            subtotal.pop(delete)
            print("Eliminar otro Producto? ")
            respuesta2 = str(input('Ingrese [ y =si / n =no ] : '))
            negativo = "n"
            if respuesta2 == negativo:
                out = True

def addCart():
    out = False
    while out == False:
        print()
        print(productos) 
        print()
        print("pulse 's' para volver")
        print()
        respuesta = str(input('Ingrese el producto elgido : '))
        if respuesta == "s":
            out = True
        else:
            iProducto = productos.index(respuesta) #obtengo el indice
            cart.append(respuesta)
            iniPrice = precios[iProducto] # paso como parametro al indice para buscar el precio
            print()
            multi = int(input('Ingrese la cantidad: '))
            print()
            item = iniPrice*multi
            subtotal.append(item)
            sumTemp = sum(subtotal) #Suma de totales temporales
            print()
            print(f"Productos agregados : {cart}")
            print()
            print(f"El subtotal es de : $ {sumTemp}")
            print()
            print("agregar otro Producto? ")
            print()
            respuesta2 = str(input('Ingrese [ y =si / n =no ] : '))
            negativo = "n"
            if respuesta2 == negativo:
                global TotalFinal
                TotalFinal = sum(subtotal)
                out = True

def cobrar():
    out = False
    while out == False:
        total = sum(subtotal)
        print("Seguro que quiere cerrar caja: ")
        print()
        respuesta = str(input('Ingrese [ y =si / n =no ] : '))
        if respuesta == "n":
            out = True
        else:
            print()    
            print("    --- Caja Cerrada --- ")
            print("--- Gracias por su Compra ---")
            print()
            print(f"La suma a Pagar es: $ {total}")
            print()
            global Sale_Final
            Sale_Final = False # Termino el Programa
            out = True

# -------------------------------------------- #
# -------------------------------------------- #

# --- Main Program --- #

while Sale_Final==True:
    print()
    print("--- Bienvenidos ---")
    print()
    print("1.- Agregar Producto.")
    print("2.- Remover Producto.")
    print("3.- Añadir a Cuenta.")
    print("4.- Quitar de la Cuenta.")
    print("5.- Cobrar.")
    print()
    totalTemp =  sum(subtotal)
    print(f"El subtotal es de : $ {totalTemp}")
    print()
    opciones = int(input('Ingrese la Opción: '))
    print()
    if opciones == 1:
        addProducts()
    if opciones == 2:
        removeProducts()
    if opciones == 3:
        addCart()
    if opciones == 4:
        removeCart()
    if opciones == 5:
        cobrar()
        
# -------------------------------------------- #
# --- Final --- #