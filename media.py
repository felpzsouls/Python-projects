qtd = 0
soma = 0
media = 0
valor = float(input("digiteum valor:"))

while (valor > 0.0):
  soma = soma + valor
  qtd = qtd + 1
  # entrada de valores
  valor = float(input("digite um valor:"))

# caso digite um valor negativo, lanço encerra

media = soma / qtd
print("\n Total da soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Media dos valores: ", media)
