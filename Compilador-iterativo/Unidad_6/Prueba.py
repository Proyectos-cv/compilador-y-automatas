cadena1 = "123"
cadena2 = "45678"

if len(cadena1) < len(cadena2):
    cadena1 = cadena1.zfill(len(cadena2))
else:
    cadena2 = cadena2.zfill(len(cadena1))

print(cadena1)
print(cadena2)
