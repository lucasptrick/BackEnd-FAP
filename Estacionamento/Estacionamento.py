from datetime import datetime, timedelta
from Veiculo import Veiculo

class Estacionamento:
    def __init__(self):
        self.veiculos = {}
        self.registro_veiculos = "registro_veiculos.txt"
        self.carregar_registros_antigos()

    def entrada_veiculo(self, placa, tipo):
        if placa not in self.veiculos:
            veiculo = Veiculo(placa, tipo)
            self.veiculos[placa] = veiculo
            with open(self.registro_veiculos, "a") as file:
                file.write(f"{placa},{tipo},{veiculo.hora_entrada}\n")
            print(f"Entrada registrada: {placa} às {veiculo.hora_entrada}")
        else:
            print(f"O veículo com a placa {placa} já está no estacionamento.")

    def saida_veiculo(self, placa):
        if placa in self.veiculos:
            veiculo = self.veiculos[placa]
            tempo_permanencia = veiculo.calcular_tempo_permanencia()
            if veiculo.gratuito:
                print(f"Veículo {placa} está liberado sem custo.")
            elif tempo_permanencia <= 20:
                print("Saída dentro dos 20 minutos permitidos. Saída liberada.")
            else:
                valor = self.calcular_valor(tempo_permanencia)
                print(f"Tempo de permanência: {tempo_permanencia:.2f} minutos. Valor a ser pago: R$ {valor:.2f}")
            del self.veiculos[placa]
        else:
            print("Veículo não encontrado.")

    def calcular_valor(self, minutos):
        # Exemplo de cálculo (R$ 5,00 por hora ou fração)
        valor = 5 * (minutos // 60 + 1)
        return valor

    def processar_pagamento(self, placa, metodo_pagamento):
        self.saida_veiculo(placa)
        print(f"Pagamento realizado via {metodo_pagamento}.")
        print("Veículo liberado para saída.")

    def conceder_gratuidade(self, placa):
        if placa in self.veiculos:
            self.veiculos[placa].gratuito = True
            print(f"Estacionamento gratuito concedido ao veículo {placa}.")
        else:
            print("Veículo não encontrado.")

    def limpar_registros_antigos(self):
        with open(self.registro_veiculos, "r") as file:
            linhas = file.readlines()
        data_limite = datetime.now() - timedelta(days=5)
        with open(self.registro_veiculos, "w") as file:
            for linha in linhas:
                placa, tipo, data_str = linha.strip().split(",")
                data_registro = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f")
                if data_registro > data_limite:
                    file.write(linha)

    def carregar_registros_antigos(self):
        try:
            with open(self.registro_veiculos, "r") as file:
                for linha in file:
                    placa, tipo, data_str = linha.strip().split(",")
                    data_registro = datetime.strptime(data_str, "%Y-%m-%d %H:%M:%S.%f")
                    self.veiculos[placa] = Veiculo(placa, tipo)
                    self.veiculos[placa].hora_entrada = data_registro
        except FileNotFoundError:
            pass