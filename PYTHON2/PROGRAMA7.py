#PROGRAMA7
#LIZETHELANDINRIOS
cantidad=int(input("INGRESA LA CANTIDAD DE PRODUCTOS"))
precio=float(input("INGRESA EL PRECIO"))
total=cantidad*precio
if (total>500):
    des=total*20
    print("SE APLICA EL 20% DE DESCUENTO",des)
else:
    des=total*10
    total=total-des
    print("SE APLICA EL 10% DE DESCUENTO",des)
    print("TOTAL A PAGAR",total)
print("FIN DEL PROGRAMA")