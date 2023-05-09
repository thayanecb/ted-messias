numeros = [0] * 20

for i in range(20):
  numeros[i] = int(input("Digite o {}º número: ".format(i+1)))

print("Números na ordem inversa:")
for i in range(19, -1, -1):
  print(numeros[i])
