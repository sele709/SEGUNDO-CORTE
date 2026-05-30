# Taller con pandas
# Autor: Jheison Cabal

import pandas as pd

# Diccionario con 60 productos, sus precios, cantidades, costos de envío y categoria
data = {
    "Producto": [
        "Laptop",
        "Mouse",
        "Teclado",
        "Silla",
        "Escritorio",
        "Monitor",
        "Tablet",
        "Impresora",
        "Scanner",
        "Disco_Duro",
        "Memoria_RAM",
        "Tarjeta_Grafica",
        "Fuente_Poder",
        "Placa_Base",
        "Procesador",
        "Ventilador",
        "Auriculares",
        "Webcam",
        "Microfono",
        "Proyector",
        "Router",
        "Switch",
        "Servidor",
        "Cable_Ethernet",
        "Adaptador_USB",
        "Bateria_Externa",
        "Cargador",
        "Soporte_Monitor",
        "Alfombrilla_Mouse",
        "Hub_USB",
        "Disco_Solido",
        "Memoria_Flash",
        "Tarjeta_Sonido",
        "Fuente_Alimentacion",
        "Placa_Video",
        "Procesador_Grafico",
        "Ventilador_Procesador",
        "Auriculares_Gaming",
        "Webcam_HD",
        "Microfono_Condensador",
        "Proyector_Portatil",
        "Router_Inalambrico",
        "Switch_Gigabit",
        "Servidor_Dedicado",
        "Cable_HDMI",
        "Adaptador_VGA",
        "Bateria_Portatil",
        "Cargador_Portatil",
        "Soporte_Laptop",
        "Alfombrilla_Gaming",
        "Hub_USB_C",
        "Disco_Solido_NVMe",
        "Memoria_Flash_USB",
        "Tarjeta_Sonido_Externa",
        "Fuente_Alimentacion_Modular",
        "Placa_Video_Gaming",
        "Procesador_Grafico_HighEnd",
        "Ventilador_Procesador_Liquid",
        "Auriculares_Gaming_7.1",
        "Webcam_4K",
    ],
    "Precio": [
        3500000,
        80000,
        120000,
        450000,
        900000,
        1100000,
        2500000,
        150000,
        200000,
        800000,
        120000,
        350000,
        150000,
        250000,
        450000,
        12000,
        85999,
        129999,
        29999,
        359999,
        459999,
        559999,
        659999,
        759999,
        859999,
        959999,
        1059999,
        1159999,
        1259999,
        1359999,
        1459999,
        1559999,
        1659999,
        1759999,
        1859999,
        1959999,
        2059999,
        2159999,
        2259999,
        2359999,
        2459999,
        2559999,
        2659999,
        2759999,
        2859999,
        2959999,
        3059999,
        3159999,
        3259999,
        3359999,
        3459999,
        3559999,
        3659999,
        3759999,
        3859999,
        3959999,
        4059999,
        4159999,
        4259999,
        3359999,
    ],
    "Cantidad": [
        4,
        15,
        10,
        5,
        3,
        6,
        8,
        12,
        18,
        7,
        14,
        6,
        8,
        12,
        4,
        16,
        24,
        36,
        48,
        58,
        68,
        78,
        88,
        98,
        108,
        118,
        5,
        9,
        13,
        17,
        21,
        25,
        29,
        33,
        37,
        41,
        45,
        49,
        2,
        6,
        10,
        14,
        18,
        22,
        26,
        30,
        34,
        38,
        42,
        46,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
    ],
    "Costo_Envio": [
        50000,
        10000,
        15000,
        20000,
        30000,
        40000,
        50000,
        60000,
        70000,
        80000,
        90000,
        100000,
        110000,
        120000,
        130000,
        140000,
        150000,
        160000,
        170000,
        180000,
        50000,
        100000,
        150000,
        50000,
        100000,
        150000,
        50000,
        10000,
        15000,
        20000,
        30000,
        40000,
        50000,
        60000,
        70000,
        80000,
        90000,
        100000,
        110000,
        120000,
        130000,
        140000,
        150000,
        160000,
        170000,
        180000,
        50000,
        100000,
        150000,
        50000,
        100000,
        150000,
        50000,
        100000,
        150000,
        50000,
        100000,
        150000,
        50000,
        100000,
    ],
    "Categoria": [
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Oficina",
        "Oficina",
        "Tecnologia",
        "Tecnologia",
        "Oficina",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Accesorios",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Oficina",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Accesorios",
        "Accesorios",
        "Accesorios",
        "Accesorios",
        "Oficina",
        "Accesorios",
        "Accesorios",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Oficina",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Accesorios",
        "Accesorios",
        "Oficina",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
        "Tecnologia",
    ],
}
# punto 1 - Creación y Exploración del DataFrame
# 1.1: generar el DataFrame utilizando pandas
df = pd.DataFrame(data)  # genera el DataFrame a partir del diccionario
print(f"DataFrame:\n{df}")  # muestra el DataFrame

# 1.2 Mostrar las primeras 5 y las 10 últimas filas del DataFrame.
print(f"Primeras 5 filas:\n{df.head()}")  # muestra las primeras 5 filas del DataFrame
print(f"Últimas 10 filas:\n{df.tail(10)}")  # muestra las últimas 10 filas del DataFrame

# 1.3 identificar el tipo de dato de cada columna
print(f"Tipos de datos:\n{df.dtypes}")  # muestra el tipo de dato de cada columna

# 1.4 Mostrar el tamaño del DataFrame (filas y columnas).
print(
    f"Tamaño del DataFrame:\n{df.shape}"
)  # muestra el tamaño del DataFrame (filas, columnas)

# 1.5 Generar una descripción estadística general del conjunto de datos.
print(
    f"Descripción estadística:\n{df.describe()}"
)  # muestra una descripción estadística general del conjunto de datos

# Punto 2 – Operaciones Matemáticas entre Columnas
# 2.1 Crear una nueva columna llamada Total_Venta = Precio × Cantidad
df["Total_Venta"] = df["Precio"] * df["Cantidad"]
print(
    f"Total_Venta:\n{df['Total_Venta']}"
)  # muestra el DataFrame con la nueva columna Total_Venta

# 2.2 crear una nueva columna llamada Costo_Total = Total_Venta + Costo_Envio.
df["Costo_Total"] = df["Total_Venta"] + df["Costo_Envio"]
print(
    f"Costo_Total:\n{df['Costo_Total']}"
)  # muestra el DataFrame con la nueva columna Costo_Total

# 2.3 Calcular el promedio del Total_Venta.
promedio_total_venta = df["Total_Venta"].mean()  # calcula el promedio de Total_Venta
print(
    f"Promedio de Total_Venta:\n{promedio_total_venta}"
)  # muestra el promedio de Total_Venta

# 2.4 Identificar el producto con mayor Total_Venta.
producto_mayor_venta = df[
    df["Total_Venta"] == df["Total_Venta"].max()
]  # identifica el producto con mayor Total_Venta
print(
    f"Producto con mayor Total_Venta:\n{producto_mayor_venta}"
)  # muestra el producto con mayor Total_Venta

# 2.5 Identificar el producto con menor Total_Venta
producto_menor_venta = df[
    df["Total_Venta"] == df["Total_Venta"].min()
]  # identifica el producto con menor Total_Venta
print(
    f"Producto con menor Total_Venta:\n{producto_menor_venta}"
)  # muestra el producto con menor Total_Venta

# Punto 3 – Porcentajes y Análisis
# 3.1 Crear una columna llamada IVA que represente el 19% del Total_Venta
df["IVA"] = df["Total_Venta"] * 0.19  # crea la columna IVA como el 19% de Total_Venta
print(f"IVA:\n{df['IVA']}")  # muestra el DataFrame con la nueva columna IVA

# 3.2 Crear una columna llamada Ganancia_Estimada correspondiente al 25% del Total_Venta
df["Ganancia_Estimada"] = (
    df["Total_Venta"] * 0.25
)  # crea la columna Ganancia_Estimada como el 25% de Total_Venta
print(
    f"Ganancia_Estimada:\n{df['Ganancia_Estimada']}"
)  # muestra el DataFrame con la nueva columna Ganancia_Estimada

# 3.3 Crear una columna llamada Perdida_Estimada correspondiente al 0.05% del Total_Venta.
df["Perdida_Estimada"] = (
    df["Total_Venta"] * 0.0005
)  # crea la columna Perdida_Estimada como el 0.05% de Total_Venta
print(
    f"Perdida_Estimada:\n{df['Perdida_Estimada']}"
)  # muestra el DataFrame con la nueva columna Perdida_Estimada

# 3.4 Calcular qué porcentaje representa cada producto respecto al total general de ventas.
total_general_ventas = df["Total_Venta"].sum()  # calcula el total general de ventas
df["Porcentaje_Ventas"] = (
    df["Total_Venta"] / total_general_ventas * 100
)  # crea la columna Porcentaje_Ventas como el porcentaje de cada producto respecto al total general de ventas
print(
    f"Porcentaje de Ventas:\n{df['Porcentaje_Ventas']}"
)  # muestra el DataFrame con la nueva columna Porcentaje_Ventas

# 3.4 Mostrar únicamente los productos cuyo porcentaje de ventas sea superior al 15%
productos_superiores_15 = df[
    df["Porcentaje_Ventas"] > 15
]  # filtra los productos cuyo porcentaje de ventas es superior al 15%
print(
    f"Productos con porcentaje de ventas superior al 15%:\n{productos_superiores_15}"
)  # muestra los productos cuyo porcentaje de ventas es superior al 15%

# Punto 4 – Estadística Descriptiva
# 4.1 Calcular la media, mediana y moda de la columna Precio
media_precio = df["Precio"].mean()  # calcula la media de la columna Precio
mediana_precio = df["Precio"].median()  # calcula la mediana de la columna Precio
moda_precio = df["Precio"].mode()[0]  # calcula la moda de la columna Precio
# imprimir los resultados de la media, mediana y moda del Precio
print(f"Media del Precio: {media_precio}")  # muestra la media del Precio
print(f"Mediana del Precio: {mediana_precio}")  # muestra la mediana del Precio
print(f"Moda del Precio: {moda_precio}")  # muestra la moda del Precio

# 4.2 Calcular la desviación estándar de la columna Cantidad.
desviacion_estandar_cantidad = df[
    "Cantidad"
].std()  # calcula la desviación estándar de la columna Cantidad
print(
    f"Desviación Estándar de la Cantidad: {desviacion_estandar_cantidad}"
)  # muestra la desviación estándar de la Cantidad

# 4.3 Calcular el valor máximo y mínimo de Total_Venta
valor_maximo_total_venta = df[
    "Total_Venta"
].max()  # calcula el valor máximo de Total_Venta
valor_minimo_total_venta = df[
    "Total_Venta"
].min()  # calcula el valor mínimo de Total_Venta
print(
    f"Valor Máximo de Total_Venta: {valor_maximo_total_venta}"
)  # muestra el valor máximo de Total_Venta
print(
    f"Valor Mínimo de Total_Venta: {valor_minimo_total_venta}\n"
)  # muestra el valor mínimo de Total_Venta

# 4.4 Explicar brevemente qué significa cada medida estadística obtenida.
print("Explicación de las medidas estadísticas obtenidas:")
print("- Media del Precio: Es el promedio de los precios de los productos.")
print("- Mediana del Precio: Es el valor central de los precios de los productos.")
print("- Moda del Precio: Es el precio que más se repite en la muestra.")
print(
    "- Desviación Estándar de la Cantidad: Mide la dispersión de las cantidades vendidas."
)
print("- Valor Máximo de Total_Venta: Es el mayor monto de venta registrado.")
print("- Valor Mínimo de Total_Venta: Es el menor monto de venta registrado.\n")

# Punto 5 – Filtrado
# 5.1 Mostrar únicamente los productos de la categoría Tecnología.
productos_tecnologia = df[
    df["Categoria"] == "Tecnologia"
]  # filtra los productos de la categoría Tecnología
print(
    f"Productos de la categoría Tecnología:\n{productos_tecnologia}"
)  # muestra los productos de la categoría Tecnología

# 5.2 Ordenar los productos de mayor a menor según Total_Venta.
productos_ordenados = df.sort_values("Total_Venta", ascending=False)
# ordena los productos de mayor a menor según Total_Venta
# ascending=False indica que el orden es de mayor a menor
print(
    f"Productos ordenados de mayor a menor según Total_Venta:\n{productos_ordenados}"
)  # muestra los productos ordenados de mayor a menor según Total_Venta

# Punto Adicional (Opcional)
# exportar el DataFrame final a un archivo CSV
df.to_csv(
    "productos_ventas.csv", index=False
)  # exporta el DataFrame a un archivo CSV sin incluir el índice
print(
    "DataFrame exportado a 'productos_ventas.csv'"
)  # confirma que el DataFrame ha sido exportado
