# Sistema Inteligente de Gestión y Reposición de Inventarios (SIGRI)

def leer_entero_no_negativo(mensaje):
    valor = int(input(mensaje))

    while valor < 0:
        print("El valor no puede ser negativo.")
        valor = int(input(mensaje))

    return valor


def mostrar_reporte_producto(sku, nombre, stock_actual, ventas,
                              mermas, estado, unidades_comprar):
    print("\n----- REPORTE DEL PRODUCTO -----")
    print("SKU:", sku)
    print("Producto:", nombre)
    print("Ventas:", ventas)
    print("Mermas:", mermas)
    print("Stock actualizado:", stock_actual)
    print("Estado:", estado)
    print("Unidades por comprar:", unidades_comprar)


# Listas para almacenar la información
lista_sku = []
lista_nombres = []
lista_stock_actual = []
lista_ventas = []
lista_mermas = []
lista_estados = []
lista_unidades_comprar = []

# Acumuladores y contadores
total_ventas = 0
total_mermas = 0
total_unidades_comprar = 0
productos_reposicion = 0

print("==============================================")
print(" SISTEMA DE GESTIÓN DE INVENTARIOS - SIGRI")
print("==============================================")

cantidad_productos = leer_entero_no_negativo(
    "Ingrese la cantidad de productos: "
)

while cantidad_productos == 0:
    print("Debe registrar por lo menos un producto.")
    cantidad_productos = leer_entero_no_negativo(
        "Ingrese la cantidad de productos: "
    )

for i in range(cantidad_productos):
    print("\nRegistro del producto", i + 1)

    sku = input("Ingrese el SKU: ")
    nombre = input("Ingrese el nombre del producto: ")

    stock_inicial = leer_entero_no_negativo(
        "Ingrese el stock inicial: "
    )
    ventas = leer_entero_no_negativo(
        "Ingrese las unidades vendidas: "
    )
    mermas = leer_entero_no_negativo(
        "Ingrese las unidades de merma: "
    )

    while ventas + mermas > stock_inicial:
        print("Las ventas y mermas no pueden superar el stock inicial.")
        ventas = leer_entero_no_negativo(
            "Ingrese nuevamente las unidades vendidas: "
        )
        mermas = leer_entero_no_negativo(
            "Ingrese nuevamente las unidades de merma: "
        )

    stock_minimo = leer_entero_no_negativo(
        "Ingrese el stock mínimo: "
    )
    stock_maximo = leer_entero_no_negativo(
        "Ingrese el stock máximo: "
    )

    while stock_maximo <= stock_minimo:
        print("El stock máximo debe ser mayor que el stock mínimo.")
        stock_maximo = leer_entero_no_negativo(
            "Ingrese nuevamente el stock máximo: "
        )

    stock_actual = stock_inicial - ventas - mermas

    if stock_actual <= stock_minimo:
        estado = "REQUIERE REPOSICIÓN"
        unidades_comprar = stock_maximo - stock_actual
        productos_reposicion = productos_reposicion + 1
    else:
        estado = "STOCK SUFICIENTE"
        unidades_comprar = 0

    lista_sku.append(sku)
    lista_nombres.append(nombre)
    lista_stock_actual.append(stock_actual)
    lista_ventas.append(ventas)
    lista_mermas.append(mermas)
    lista_estados.append(estado)
    lista_unidades_comprar.append(unidades_comprar)

    total_ventas = total_ventas + ventas
    total_mermas = total_mermas + mermas
    total_unidades_comprar = total_unidades_comprar + unidades_comprar

    mostrar_reporte_producto(
        sku, nombre, stock_actual, ventas,
        mermas, estado, unidades_comprar
    )

print("\n==============================================")
print("              REPORTE GENERAL")
print("==============================================")

for i in range(cantidad_productos):
    print("\nProducto", i + 1)
    print("SKU:", lista_sku[i])
    print("Nombre:", lista_nombres[i])
    print("Stock actual:", lista_stock_actual[i])
    print("Estado:", lista_estados[i])
    print("Unidades por comprar:", lista_unidades_comprar[i])

porcentaje_criticos = (
    productos_reposicion / cantidad_productos
) * 100

mayor_merma = max(lista_mermas)
posicion_mayor_merma = lista_mermas.index(mayor_merma)

print("\n--------------- INDICADORES ----------------")
print("Productos registrados:", cantidad_productos)
print("Productos que requieren reposición:", productos_reposicion)
print("Productos que requieren reposición:", [lista_nombres[i] for i in range(cantidad_productos) if lista_estados[i] == "REQUIERE REPOSICIÓN"])
print("Productos con stock suficiente:",
      cantidad_productos - productos_reposicion)
print("Total de unidades vendidas:", total_ventas)
print("Total de mermas:", total_mermas)
print("Total de unidades por comprar:", total_unidades_comprar)
print("Porcentaje de productos críticos:",
      round(porcentaje_criticos, 2), "%")
print("Producto con mayor merma:",
      lista_nombres[posicion_mayor_merma])
print("Cantidad de mayor merma:", mayor_merma)
print("==============================================")
