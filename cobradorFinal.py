

#Listas Principales
productos = []
precios = []
indices = []
subtotal = []

# Variables Globales
auxi1 = ""
auxi2 = ""
items = 0
salida = False
Sale_Final = True

#Funciones
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

def cantidades(precio, cantidad):
    return precio*cantidad

def addProducts():
    out = False
    while out == False:
        paquete = agregar_producto() # guardo producto
        productos.append(paquete)
        indice1 = (productos.index(auxi1))
        indices.append(indice1)
        print(indice1)

        monto = agregar_precio()        # guardo precio
        precios.append(monto)           # agrego precio
        #indice2 = (precios.index(auxi2))
        #print(indice2)

        print("<- Productos Agregados ->")
        print(f"Productos: {productos}")
        print(f"precios:    ${precios}")
        print(f"Id's        {indices}")
            
        print("Agregar mas Productos? ")
        respuesta = str(input('Ingrese [ y =si / n =no ] : '))
        negativo = "n"
        if respuesta == negativo:
           out = True
    product = str(input('Nombre del Producto: '))


def remove(lista, producto):
    item = str(producto)
    delete = (lista.index(item))
    lista.pop(delete)

def removeProducts():
    out = False
    while out == False:
        print(productos)
        print()
        print("s para volver")
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

# --- Main Program --- #

while Sale_Final==True:
    print(" Bienvenidos ")
    print("1.-Agregare Producto.")
    print("2.-Remover Producto.")
    print("3.-Añadir a Cuenta.")
    print("4.-Quitar de la Cuenta.")
    print("5.-Cobrar.")
    opciones = int(input('Ingrese la Opción: '))
    if opciones == 1:
        addProducts()
    if opciones == 2:
        removeProducts()
        #elif opciones == 3:
            #addcart
        #elif opciones == 4:
            #removeCart
    if opciones == 5:
        total = sum(precios)
        print(f"La suma a Pagar es: $ {total}")
        Sale_Final = False

# --- Final --- #
