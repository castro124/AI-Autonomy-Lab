# Ejercicio 03 - Strings

nombre = "Juan"
apellido = "Castro"

# Concatenación
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# f-string (la forma moderna y correcta)
edad = 25
presentacion = f"Me llamo {nombre} {apellido} y tengo {edad} años"
print(presentacion)

# Métodos de strings

print(nombre.upper())
print(nombre.lower())
print(nombre_completo.replace("Carlos", "Juan"))
print(len(nombre_completo))

# Indexing

print(nombre[0])
print(nombre[-1])
print(nombre[0:3])


