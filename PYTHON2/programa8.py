#PROGRAMA8
#LIZETHELANDINRIOS
pagodia=int(input("Ingrese el pago x dia"))
diatra=int(input("Ingrese dias trabajados"))
tx=(input("¿Trabajo dias extras?"))
if (tx=="si") or (tx=="SI") :
    diaextra=int(input("Ingrese dias extras trabjados"))
    pagoextra=int(input("Ingrese pago x dias extras trabajados"))
    total=pagodia*diatra
    extra=pagoextra*diaextra
    print("El pago es: ",total)
    print("El pago por dias extras es:",extra)
else:
    total=pagodia*diatra
    print("El pago es:",total)
print("FIN DEL PROGRAMA")