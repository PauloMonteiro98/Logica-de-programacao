# 10. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float(input('Informe a temperatura em graus Fahrenheit: '))
c = 5 * ((f-32) / 9)

print(f'A conversão de graus Fahrenheit para graus Celsius é: {c:.2f} ºC')

