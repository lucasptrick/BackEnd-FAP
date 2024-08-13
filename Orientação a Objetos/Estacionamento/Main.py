from Estacionamento import Estacionamento
from datetime import datetime



def exibir_menu():
    print("\n--- Sistema de Gerenciamento de Estacionamento ---")
    print("1. Registrar entrada de veículo")
    print("2. Processar saída de veículo")
    print("3. Conceder gratuidade")
    print("4. Limpar registros antigos")
    print("5. Sair")

def main():
    estacionamento = Estacionamento()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa do veículo: ").upper()
            tipo = input("Digite o tipo do veículo (Carro/Moto): ").capitalize()
            estacionamento.entrada_veiculo(placa, tipo)

        elif opcao == "2":
            placa = input("Digite a placa do veículo: ").upper()
            metodo_pagamento = input("Digite o método de pagamento (Pix/Débito/Crédito/Dinheiro): ").capitalize()
            estacionamento.processar_pagamento(placa, metodo_pagamento)

        elif opcao == "3":
            placa = input("Digite a placa do veículo para conceder gratuidade: ").upper()
            estacionamento.conceder_gratuidade(placa)

        elif opcao == "4":
            estacionamento.limpar_registros_antigos()
            print("Registros antigos foram limpos.")

        elif opcao == "5":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
