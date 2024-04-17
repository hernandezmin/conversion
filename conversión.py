def segundos_a_minutos():
    segundos= float(input("ingrese los segundos a convertir"))
    return segundos/60

def minutos_a_horas():
    minutos= float(input("ingrese los minutos a convertir"))
    return minutos/60

def horas_a_segundos():
    horas= float(input("ingrese las horas a convertir"))
    return horas/3600



print("Bienvenido al conversor de tiempo")
print("1. Segundos a minutos, 2. Minutos a horas, 3. Horas a segundos")

opcion=input("¿Qué tipo de conversión quiere realizar?")

if opcion == "1":
    print(segundos_a_minutos())

if opcion == "2":
    print(minutos_a_horas())

if opcion == "3":
    print(horas_a_segundos())




