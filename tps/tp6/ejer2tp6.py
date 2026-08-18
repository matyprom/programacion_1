inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}
productos_bajo_stock={}
valor_total={}
reposicion_inmediata={}
for productos, datos in inventario.items():
    if datos["stock"]<5:
        productos_bajo_stock[productos]=datos["stock"]
                
        #print(f"el producto {productos} tiene {cantidad} unidades")
    valor_total[productos]=datos["precio"]*datos["stock"]
    if datos["stock"]<=2:
        reposicion_inmediata[productos]=datos["stock"]
            
print(valor_total)
print(productos_bajo_stock)
print(reposicion_inmediata)