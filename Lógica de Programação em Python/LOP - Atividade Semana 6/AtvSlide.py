def opcao1(lista):
    print(f"Média dos valores: {sum(lista)/len(lista)}")

def opcao2(lista):
    print(f"Soma dos valores: {sum(lista)}")

def opcao3(lista):
    print(f"Maior elemento: {max(lista)}")

def opcao4(lista):
    print(f"Menor elemento: {min(lista)}")

listaValores = []
for valor in range(8):
    entradaUsuario = int(input(f"Digite o {valor+1}º valor:"))
    listaValores.append(entradaUsuario)

menu = input(f"Escolha uma opção:\n1. Calcular média\n2. Calcular soma\n3.Calcular o maior\n4. calcular o menor.\n>>")
if(menu == '1'):
    opcao1(listaValores)
elif(menu == '2'):
    opcao2(listaValores)
elif(menu == '3'):
    opcao3(listaValores)
elif(menu == '4'):
    opcao4(listaValores)
else:
    print(f"Opção inválida!")
