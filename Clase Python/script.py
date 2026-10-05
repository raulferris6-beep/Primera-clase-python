persona = {
    "nombre": "Raul",
    "edad": 20,
    "ciudad": "Albal",
    "soltero": True
}
print(persona["nombre"])


compra = ["pan", "leche", "huevos"]

compra.append("frutas")

compra.insert(2, "verduras")

compra.pop()

print(compra)

culpable = False

if culpable:
    print("Es culpable")
else:
    print("No es culpable")