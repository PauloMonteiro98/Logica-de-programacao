# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorhora = float(input('Informe o valor ganho por hora: '))
horasmes = float(input('Informe o número de horas trabalhadas no mês: '))
salario = valorhora*horasmes

print(f'Você ganhou R$ {salario:.2f} nesse mês.')