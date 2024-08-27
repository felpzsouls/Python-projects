notaA = float(input('informe a primeira nota'))
notaB = float(input("informe a segunda nota"))

mediaFinal =(notaA + notaB) / 2

if mediaFinal >= 7.0:
  print("a média: %.1f Aprovado" % mediaFinal);
else:
  print("a média: %.1f Reprovado" % mediaFinal);
