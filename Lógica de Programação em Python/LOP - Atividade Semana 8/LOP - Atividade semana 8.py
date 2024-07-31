'Ex 01:' 
'Faça um programa que receba do usuário um arquivo e mostre na tela quantas linhas esse arquivo possui.'
#arquivoUser = open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt","r")
#print(f"Qtde linhas no arquivo: {len(arquivoUser.readlines())}")
#arquivoUser.close()


'Ex 02'
'Faça um progama que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais'
#cont = 0
#arquivoUser = open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", "r")
#for word in arquivoUser.readlines():
#    for char in word.lower():
#        if char in 'aeiouàáôóêéíúüçãõ':
#            cont+=1
#print(f"Qtde vogais no arquivo:{cont}")
#arquivoUser.close()


'Ex 03'
'Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras são vogais e quantas são consoantes.'
#contVogais = 0
#contConsoantes = 0
#arquivoUser = open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", "r")
#for word in arquivoUser.readlines():
#    for char in word.lower():
#        if char in 'aeiouâàáôóêéíúüãõ':
#            contVogais+=1
#        else:
#            if char.isalpha() and char != 'aeiouâàáôóêéíúüãõ':
#                contConsoantes+=1
#
#print(f"Qtde vogais no arquivo:{contVogais}\nQtde consoantes no arquivo:{contConsoantes}")
#arquivoUser.close()


'Ex 04'
'Faça um programa que receba do usuário um arquivo texto e um caracter. Mostre na tela quantas vezes aquele caractere ocorre dentro do arquivo.'
#contCaracter = 0
#caracter = input("Digite um caracter que você desejar contar: ").lower()
#arquivoUser = open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", "r")
#for word in arquivoUser.readlines():
#    for char in word.lower():
#        if char == caracter:
#            contCaracter+=1

#print(f"Qtde do caracter informado: {contCaracter}")        
#arquivoUser.close()

'Ex 05'
'Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes cada letra do alfabeto aparece dentro do arquivo.'
#alfabeto = 'abcdefghijklmnopqrstuvwxyz'
#cont = {letra: 0 for letra in alfabeto}
#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", "r", encoding="utf-8") as text:
#    arquivoUser = text.read().lower()
#for char in arquivoUser:
#    if char in cont:
#        cont[char]+=1
#for letra, qtde in cont.items():
#    print(f"{letra}: {qtde}")


'Ex 06'
'Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo o texto do arquivo de entrada, mas com as vogais substituídas por "**.'
#vogais = 'aeiouàáôóêéíúüãõAEIOUÀÁÔÓÊÉÍÚÜÃÕ'
#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", "r", encoding="utf-8") as arquivoUser:
#    texto = arquivoUser.read()

#textoModificado = ''.join('*' if char in vogais else char for char in texto)

#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/ArquivoNovo.txt", "w", encoding="utf-8") as arquivoNovo:
#    arquivoNovo.write(textoModificado)


'Ex 07'
'Desenvolver um programa que leia o conteúdo de um arquivo e cria um arquivo com o mesmo conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário.'
#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", "r", encoding='utf-8') as arquivoUser:
#    texto = arquivoUser.read().upper() 

#nomeDoArquivo = input("Digite um nome para o novo arquivo: ")
#caminhoNovoArquivo = f"C:\\Users\\lpro\\Documents\\PtrckSpace\\Exercícios\\{nomeDoArquivo}.txt"

#with open(caminhoNovoArquivo, "w", encoding="utf-8") as arquivoNovo:
#    arquivoNovo.write(texto)  


'Ex 08' 
'Faça um programa que receba dois arquivos do usuário, e crie um terceiro arquivo com o conteúdo dos dois primeiros juntos (o conteúdo do primeiro seguido do conteúdo do segundo).'
#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt","r", encoding="utf-8") as arquivoUser1:
#    text1 = arquivoUser1.read()

#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/testeSecundario.txt","r", encoding="utf-8") as arquivoUser2:
#    text2 = arquivoUser2.read()

#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/arquivoSaida.txt","w", encoding="utf-8") as arquivoSaida:        
#        arquivoSaida.write(text1)
#        arquivoSaida.write("\n")
#        arquivoSaida.write(text2)


'Ex 09'
'Faça um programa que receba como entrada o nome de um arquivo de entrada e outro de saída. O arquivo de entrada contém em cada linha o nome de uma cidade (ocupando 40 caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de entrada e gerar um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número de habitantes.'
#arquivoSaida = input('Digite um nome para o arquivo de saída:')
#maiorPopulacao = 0
#cidadePopulosa = ''

#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/cidades.txt", "r", encoding="utf-8") as aEntrada:
#    for linha in aEntrada:
#        linha = linha.strip()
#        if not linha:
#            continue

#        partes = linha.rsplit(' ', 1)
#        if len(partes) < 2:
#            continue 

#        cidade = partes[0]
#        try:
#            populacao = int(partes[1])
#        except ValueError:
#            continue  

#        if populacao > maiorPopulacao:
#            maiorPopulacao = populacao
#            cidadePopulosa = cidade

#with open(arquivoSaida, "w", encoding="utf-8") as aSaida:
#    aSaida.write(f"{cidadePopulosa} : {maiorPopulacao}\n")


'Ex 10'
'Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne o número de vezes que aquela palavra aparece no arquivo.'
#palavra = input("Informe a palavra a ser contada: ")
#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", 'r', encoding='utf-8') as arquivo:
#            conteudo = arquivo.read()
#            contagem = conteudo.lower().split().count(palavra.lower())

#print(f"A palavra '{palavra}' aparece {contagem} vezes no arquivo.")


'Ex 11'
'Abra um arquivo texto, calcule e escreva o número de caracteres, o número de linhas e o número de palavras neste arquivo. Escreva também quantas vezes cada letra ocorre no arquivo (ignorando letras com acento). Obs.: palavras são separadas por um ou mais caracteres espaço, tabulação ou nova linha.'
import re
from collections import Counter
#with open("/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/teste.txt", 'r', encoding='utf-8') as arquivo:
#    conteudo = arquivo.read()

    # Contar caracteres
#    num_caracteres = len(conteudo)
    
    # Contar linhas
#    num_linhas = conteudo.count('\n') + 1
    
    # Contar palavras
#    palavras = re.split(r'\s+', conteudo)
#    num_palavras = len(palavras)
    
    # Função para remover acentos
#    def remover_acentos(txt):
#        return re.sub(
#            r'[áàâãäåéèêëíìîïóòôõöúùûüýÿñç]',
#            lambda match: {
#                'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'å': 'a',
#                'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
#                'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
#                'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
#                'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
#                'ý': 'y', 'ÿ': 'y', 'ñ': 'n', 'ç': 'c'
#            }[match.group(0)],
#            txt
#        )
    
    # Contar letras
#    conteudo_sem_acentos = remover_acentos(conteudo.lower())
#    letras = re.findall(r'[a-z]', conteudo_sem_acentos)
#    contagem_letras = Counter(letras)

# Imprimir resultados
#print(f"Número de caracteres: {num_caracteres}")
#print(f"Número de linhas: {num_linhas}")
#print(f"Número de palavras: {num_palavras}")
#print("Contagem de cada letra:")
#for letra, contagem in sorted(contagem_letras.items()):
#    print(f"{letra}: {contagem}")


'Ex 12'
'Faça um programa que permita que o usuário entre com diversos nomes e telefone para cadastro, e crie um arquivo com essas informações, uma por linha. O usuário finaliza a entrada com "0" para o telefone.'
#nome_arquivo = input("Informe o nome do arquivo para salvar os contatos: ")
#if not nome_arquivo.endswith('.txt'):
#    nome_arquivo += '.txt'

#caminho_de_salvar_arquivos = f"/home/lucasptrick/Documentos/Ptrck-Space/BackEnd-FAP/Lógica de Programação em Python/LOP - Atividade semana 8/{nome_arquivo}"
#with open(caminho_de_salvar_arquivos, 'w', encoding='utf-8') as arquivo:
#    while True:
#        nome = input("Informe o nome: ")
#        telefone = input("Informe o telefone (ou '0' para finalizar): ")
#        if telefone == '0':
#            break
#        arquivo.write(f"{nome}: {telefone}\n")
#    print(f"Contatos salvos no arquivo {nome_arquivo}.")