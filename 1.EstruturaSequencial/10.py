#10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"A temperatura de {celsius}°C é equivalente a {fahrenheit:.2f}°F.")