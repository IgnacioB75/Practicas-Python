# Arrays
meses_30 = [ 4, 6, 9, 11] # Meses que tienen 30 días
meses_31 = [ 1, 3, 5, 7, 8, 10, 12] # Meses que tienen 31 días
meses = ["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] # Array de los meses del año

numero_mes = int(input("Ingresa un número de mes (1-12): ")) # Input del número del mes
print("El número de mes introducido:", numero_mes) # Mostrarle al usuario su elección

# Función
while True:

    if numero_mes in meses_30: 
        print("El mes tiene 30 días")
    elif numero_mes in meses_31: 
        print("El mes tiene 31 días")
    elif numero_mes == 2:
        print("El mes es febrero")
        break
    else:
        print("Número de mes no válido")
        break

    print(meses[numero_mes - 1]) # Imprime el nombre del mes seleccionado
    break # Termina la función

# Testing: numero_mes = -1|0|2|4|5|13 