vet = [0] * 10

for i in range(10):
  vet[i] = int(input("Digite o {}º número: ".format(i+1)))

repetidos = []
for i in range(len(vet)):
  if vet[i] in vet[i+1:] and vet[i] not in repetidos:
    repetidos.append(vet[i])
    print("O número {} se repete nas posições:".format(vet[i]))
    for j in range(i, len(vet)):
      if vet[j] == vet[i]:
        print(j)

if not repetidos:
  print("Não foram encontrados números repetidos.")
