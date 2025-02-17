#10.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        #a)o produto do dobro do primeiro com metade do segundo .
        #b)a soma do triplo do primeiro com o terceiro.
        #c)o terceiro elevado ao cubo.

numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite o número real: "))

produto = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
soma = (3 * numero_inteiro1) + numero_real
terceiro_cubo = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro número elevado ao cubo é: {terceiro_cubo:.2f}")