#17.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
#   pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
#   latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
        #a)comprar apenas latas de 18 litros;
        #b)comprar apenas galões de 3,6 litros;
        #c)misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
        #   arredonde os valores para cima, isto é, considere latas cheias.

import math

def calcular_tinta(area):
    cobertura_por_litro = 6
    litros_necessarios = area / cobertura_por_litro
    litros_com_folga = litros_necessarios * 1.10
    latas_necessarias = math.ceil(litros_com_folga / 18)
    galoes_necessarios = math.ceil(litros_com_folga / 3.6)
    preco_latas = latas_necessarias * 80
    preco_galoes = galoes_necessarios * 25
    latas_para_mistura = math.floor(litros_com_folga / 18)
    galoes_para_mistura = math.ceil((litros_com_folga - latas_para_mistura * 18) / 3.6)
    preco_mistura = latas_para_mistura * 80 + galoes_para_mistura * 25
    return latas_necessarias, preco_latas, galoes_necessarios, preco_galoes, latas_para_mistura, galoes_para_mistura, preco_mistura

area = float(input("Informe o tamanho da área a ser pintada (em metros quadrados): "))

latas, preco_latas, galoes, preco_galoes, latas_mistura, galoes_mistura, preco_mistura = calcular_tinta(area)

print(f"\nSituação 1: Comprar apenas latas de 18 litros:")
print(f"Quantidade de latas: {latas} lata(s), Preço: R$ {preco_latas:.2f}")

print(f"\nSituação 2: Comprar apenas galões de 3,6 litros:")
print(f"Quantidade de galões: {galoes} galão(ões), Preço: R$ {preco_galoes:.2f}")

print(f"\nSituação 3: Misturar latas e galões (com desperdício mínimo):")
print(f"Quantidade de latas: {latas_mistura} lata(s), Quantidade de galões: {galoes_mistura} galão(ões), Preço: R$ {preco_mistura:.2f}")
