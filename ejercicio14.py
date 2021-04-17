peso = int(input("ingrese la cantidad de monedas de un peso:"))
medioPeso = int(input("ingrese la cantidad de monedas de un medio peso:"))
cuartoPeso = int(input("ingrese la cantidad de monedas de un cuarto peso:"))
centimoPeso = int(input("ingrese la cantidad de monedas de 10 centavos:"))
cincoCentavo = int(input("ingrese la cantidad de monedas de 5 centavos:"))
total = peso + medioPeso * 0.5 + cuartoPeso*0.25 + centimoPeso*0.1 + cincoCentavo*0.05
print("el banco tiene:", total, "pesos")