lista = []

def inserir(veiculo, horarioEntrada):
    lista.append({'veiculo': veiculo, 'horarioEntrada': horarioEntrada})
    #print(f"Veículo {veiculo} entrou às {horarioEntrada}.")


def remover(veiculo, horarioSaida):
    if veiculo in lista: #Checa se o veiculo está no estacionamento
            if (lista - horarioSaida): #horarioSaida < 10: #Checa se o tempo de estacionamento ultrapassa 10Min
                #print(f"Valor de Estacionamento: {valorVaga + 2}")
                lista.remove({'Veículo': veiculo, 'Horário de Entrada': horarioSaida})
            else:
                print(f"Valor de Estacionamento: {2 +2 }") #valorVaga
    else:
        print(f"O veículo \nMarca:{veiculo.marca} - Modelo:{veiculo.modelo}\n Não está em nosso estacionamento!")

inserir('Uno',13)
inserir('Opala',14)
inserir('Ferrari',15)

#for i in range(len(lista)):
print(lista[1])
