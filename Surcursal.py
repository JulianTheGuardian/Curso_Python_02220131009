print("Ingrese los nombres de los productos:")
p = str(input("#1: "))
p1 = str(input("#2: "))
p2 = str(input("#3: "))
p3 = str(input("#4: "))
p4 = str(input("#5: "))

print("\nDigite el precio de los productos")
v = int(input(p + ": "))
v1 = int(input(p1 + ": "))
v2 = int(input(p2 + ": "))
v3 = int(input(p3 + ": "))
v4 = int(input(p4 + ": "))

print("\nEn la surcursal #1 cual fue la cantidad que se vendio de los productos")
a = int(input(p + ": "))
a1 = int(input(p1 + ": "))
a2 = int(input(p2 + ": "))
a3 = int(input(p3 + ": "))
a4 = int(input(p4 + ": "))

print("\nEn la surcursal #2 cual fue la cantidad que se vendio de los productos")
b = int(input(p + ": "))
b1 = int(input(p1 + ": "))
b2 = int(input(p2 + ": "))
b3 = int(input(p3 + ": "))
b4 = int(input(p4 + ": "))

print("\nEn la surcursal #3 cual fue la cantidad que se vendio de los productos")
c = int(input(p + ": "))
c1 = int(input(p1 + ": "))
c2 = int(input(p2 + ": "))
c3 = int(input(p3 + ": "))
c4 = int(input(p4 + ": "))

print("\nEn la surcursal #4 cual fue la cantidad que se vendio de los productos")
d = int(input(p + ": "))
d1 = int(input(p1 + ": "))
d2 = int(input(p2 + ": "))
d3 = int(input(p3 + ": "))
d4 = int(input(p4 + ": "))



cantidadTotal = a+b+c+d
cantidadTotal1 = a1+b1+c1+d1
cantidadTotal2 = a2+b2+c2+d2
cantidadTotal3 = a3+b3+c3+d3
cantidadTotal4 = a4+b4+c4+d4

cantidadS2 = b+b1+b2+b3+b4

recaudacion = (a+b+c+d)*v
recaudacion1 = (a1+b1+c1+d1)*v1
recaudacion2 = (a2+b2+c2+d2)*v2
recaudacion3 = (a3+b3+c3+d3)*v3
recaudacion4 = (a4+b4+c4+d4)*v4

rcsurcursal1 = (a*v) + (a1*v1) + (a2*v2) + (a3*v3) + (a4*v4)
rcsurcursal2 = (b*v) + (b1*v1) + (b2*v2) + (b3*v3) + (b4*v4)
rcsurcursal3 = (c*v) + (c1*v1) + (c2*v2) + (c3*v3) + (c4*v4)
rcsurcursal4 = (d*v) + (d1*v1) + (d2*v2) + (d3*v3) + (d4*v4)

rcempresa = recaudacion + recaudacion1 + recaudacion2 + recaudacion3 + recaudacion4


print("\nLas cantidad total del producto " + p + " fue " + str(cantidadTotal))
print("Las cantidad total del producto " + p1 + " fue " + str(cantidadTotal1))
print("Las cantidad total del producto " + p2 + " fue " + str(cantidadTotal2))
print("Las cantidad total del producto " + p3 + " fue " + str(cantidadTotal3))
print("Las cantidad total del producto " + p4 + " fue " + str(cantidadTotal4))
print("\nLa cantidad de articulos de la surcursal #2 son " + str(cantidadS2))
print("\nLa cantidad de " + p2 + " en la surcursal 1 es de " + str(a2))
print("\nLa recaudacion total de cada surcursal es de")
print("Se recaudo " + str(rcsurcursal1) + " en la surcusal 1")
print("Se recaudo " + str(rcsurcursal2) + " en la surcusal 2")
print("Se recaudo " + str(rcsurcursal3) + " en la surcusal 3")
print("Se recaudo " + str(rcsurcursal4) + " en la surcusal 4")
print("La reacaudacion total de la empresa en general fue de " + str(rcempresa))


if rcsurcursal1 > rcsurcursal2 and rcsurcursal1 > rcsurcursal3 and rcsurcursal1 > rcsurcursal4:
    print("La surcursal numero 1 es la que mayor recaudacion tuvo")

elif rcsurcursal2 > rcsurcursal1 and rcsurcursal2 > rcsurcursal3 and rcsurcursal2 > rcsurcursal4:
    print("La surcursal numero 2 es la que mayor recaudacion tuvo")

elif rcsurcursal3 > rcsurcursal1 and rcsurcursal3 > rcsurcursal2 and rcsurcursal3 > rcsurcursal4:
    print("La surcursal numero 3 es la que mayor recaudacion tuvo")

else:
    print("La surcursal numero 4 es la que mayor recaudacion tuvo")
