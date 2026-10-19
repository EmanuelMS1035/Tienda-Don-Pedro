from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")

productos = lineas[2:]
total_productos = 0
valor_inventario = 0

for linea in productos:
    print("-", linea)

    partes = linea.split("|")
    if len(partes) >= 2:
        precio = int(partes[-1].strip())
        total_productos += 1
        valor_inventario += precio

print("Total de productos:", total_productos)
print(f"Valor del inventario: ${valor_inventario}")