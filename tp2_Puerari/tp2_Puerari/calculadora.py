while True:
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))

    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    if num2 != 0:
        divi = num1 / num2
    else:
        divi = "No se puede dividir por cero"
    
    
    operacion = input("¿Que operacion queres realizar? ")
    if operacion == "suma":
        print (suma)
    elif operacion == "resta":
        print (resta)
    elif operacion == "multiplicacion":
        print (multi)
    elif operacion == "division":
        print (divi)
    
    print("Resultado de la suma:", suma)
    print("Resultado de la resta:", resta)
    print("Resultado de la multiplicación:", multi)
    print("Resultado de la división:", divi)
    