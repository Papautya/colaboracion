print ('Bienvenidos al entremaniemto de PYTHON')

"""
Descuento de la compra:
Si compras mas de 1000 obtienes un descuento del 20%
Pide el monto de la compra y muestra el precio final.
"""

compra = float(input("Por favor digita el valor de la compra: "))


descuento = 20
if (compra >= 1000):
    operacion = compra*descuento/100
    a_pagar = compra - operacion
    print(f"Tienes el descuento del 20% ({operacion}) y el valor a pagar es: {a_pagar}")
else:
    print("No tienes ningun descuento")