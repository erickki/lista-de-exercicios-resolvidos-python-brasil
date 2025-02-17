#16.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
#   pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
#   latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
#   preço total.

import math

area = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

cobertura_por_litro = 3
litros_por_lata = 18
preco_por_lata = 80.00

litros_necessarios = area / cobertura_por_litro
latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)
preco_total = latas_necessarias * preco_por_lata

print(f"Para pintar {area} metros quadrados, você precisará de {latas_necessarias} lata(s) de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")
