'Ex 1'
#num01 = int(input("Digite o primeiro número: "))
#num02 = int(input("Digite o segundo número: "))
#num03 = int(input("Digite o terceiro número: "))

#if num01 >= num02 >= num03:
#    maior, meio, menor = num01, num02, num03
#elif num01 >= num03 >= num02:
#    maior, meio, menor = num01, num03, num02
#elif num02 >= num01 >= num03:
#    maior, meio, menor = num02, num01, num03
#elif num02 >= num03 >= num01:
#    maior, meio, menor = num02, num03, num01
#elif num03 >= num01 >= num02:
#    maior, meio, menor = num03, num01, num02
#elif num03 >= num02 >= num01:
#    maior, meio, menor = num03, num02, num01

#print(f"Os números em ordem decrescente são: {maior} - {meio} - {menor}")

'Ex 2'
#codigoProduto = int(input("Digite o código do produto: "))

#if codigoProduto == 1:
#    print("Alimento não-perecível")
#elif codigoProduto >= 2 and codigoProduto <= 4:
#    print("Alimento perecível")
#elif codigoProduto == 5 or codigoProduto == 6:
#    print("Vestuário")
#elif codigoProduto == 7:
#    print("Higiene Pessoal")
#elif codigoProduto>= 8 and codigoProduto <= 15:
#    print("Limpeza e Utensílios Domésticos")
#else:
#    print("Inválido")

'Ex 3'
#nota1 = float(input("Digite sua nota 1:"))
#nota2 = float(input("Digite sua nota 2:"))
#nota3 = float(input("Digite sua nota 3:"))

#calc = (nota1+nota2+nota3)/3

#if calc >= 7:
#    print(f"Aprovado - Média {calc}")
#elif calc <= 7 and calc >= 4:
#    print(f"Em prova final - Média {calc}")
#else:
#    print(f"Reprovado - Média {calc}")

'Ex 4'
#num01 = float(input("Digite o primeiro número: "))
#num02 = float(input("Digite o segundo número: "))
#num03 = float(input("Digite o terceiro número: "))

#opcao = int(input('''Escolha uma opção abaixo:
#    2 - Soma dos números
#    3 - Produto dos números
#    4 - Checando o maior\n>> '''))

#if (opcao == 2):
#    print(f"{num01+num02+num03}")
#elif (opcao == 3):
#    print(f"{num01*num02*num03}")
#elif (opcao == 4):
#    calc = (num01+num02)
#    if (calc > num03):
#        print("Num1 + Num2 é maior que Num3")
#    elif (calc < num03):
#        print("Num1 + Num2 é menor que Num3")
#    elif (calc == num03):
#        print("Num1 + Num2 é igual ao Num3")
#else:
#    print("Opção invalida!")

'Ex 5'
#dia = int(input("Digite o dia do seu nascimento:"))
#mes = int(input("Digite o mês do seu nascimento:"))
#ano = int(input("Digite o ano do seu nascimento:"))

#calcAno = 2024 - ano
#calcMes = 6 - mes
#calcDias = 26 - dia

#if calcDias < 0:
#    calcDias += 30
#    calcMes -= 1
#if calcMes < 0:
#    calcMes += 12
#    calcAno -= 1

#totalDias = calcAno * 360 + calcMes * 30 + calcDias
#print(f"Você já viveu: {totalDias}")