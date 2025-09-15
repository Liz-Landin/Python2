#PROGRAMA1
#LIZETHELANDINRIOS
edad=int(input("Ingrese la edad: "))
precio=float(input("Ingrese el precio: "))
if (edad>=1) and (edad<=12):
    des=precio*0.50
    print("El precio es: $",des)
if (edad>=13) and (edad<=17):
    des=precio*0.70
    print("El precio es: $",des)
if (edad>=18) and (edad<=59):
    des=precio*0.80
    print("El precio es: $",des)
if edad>=60:
    des=precio*0
    print("Pasa gratis")
print("FIN DEL PROGRAMA")