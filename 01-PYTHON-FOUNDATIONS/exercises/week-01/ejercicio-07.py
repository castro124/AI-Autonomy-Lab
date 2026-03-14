nombre = input("¿Cómo te llamas? ")
año_nacimiento = int(input("¿En qué año naciste? "))
altura = float(input("¿Cual es tu altura en metros? "))

edad = 2026 - año_nacimiento

print(f"Tu edad aproximada es: {edad} años.")
print(f"Tu altura es de: {altura * 100} cm.")

if edad >= 18:
    print(True)
else:
    print(False)
    
print(f"Tu nombre es: {nombre}, tienes {edad} años y tu altura es de {altura * 100} cm.")
