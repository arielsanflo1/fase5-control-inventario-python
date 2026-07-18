"""
Fase 5 - Evaluacion Final POA
Curso: Fundamentos de Programacion - Codigo 213022
Problema 3: Auditoria y reabastecimiento de inventario
Autor: Ariel Sandoval Florez
"""


def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """Calcula la cantidad que debe solicitarse para alcanzar el stock minimo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def generar_informe(inventario):
    """Recorre la matriz de inventario, calcula pedidos y muestra el informe."""
    total_articulos = 0
    articulos_por_reabastecer = 0
    unidades_totales_a_pedir = 0

    print("=" * 88)
    print("INFORME DE AUDITORIA Y REABASTECIMIENTO DE INVENTARIO".center(88))
    print("=" * 88)
    print(f"{'CODIGO':<10}{'ARTICULO':<32}{'ACTUAL':>10}{'MINIMO':>10}{'PEDIR':>10}{'ESTADO':>16}")
    print("-" * 88)

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_pedir(stock_actual, stock_minimo)

        if cantidad_pedir > 0:
            estado = "Reabastecer"
            articulos_por_reabastecer += 1
        else:
            estado = "Suficiente"

        total_articulos += 1
        unidades_totales_a_pedir += cantidad_pedir

        print(
            f"{codigo:<10}{nombre:<32}{stock_actual:>10}"
            f"{stock_minimo:>10}{cantidad_pedir:>10}{estado:>16}"
        )

    print("-" * 88)
    print(f"Total de articulos auditados: {total_articulos}")
    print(f"Articulos que requieren reabastecimiento: {articulos_por_reabastecer}")
    print(f"Unidades totales que se deben pedir: {unidades_totales_a_pedir}")
    print("=" * 88)


def main():
    # Matriz: [Codigo, Nombre, Stock actual, Stock minimo requerido]
    inventario = [
        ["ART001", "Sombrero Dallas", 4, 10],
        ["ART002", "Sombrero Stetson 5X", 12, 8],
        ["ART003", "Caja para sombrero", 5, 15],
        ["ART004", "Cinta decorativa", 20, 20],
        ["ART005", "Producto de limpieza", 3, 7],
        ["ART006", "Bolsa de empaque", 25, 30],
    ]

    generar_informe(inventario)


if __name__ == "__main__":
    main()
