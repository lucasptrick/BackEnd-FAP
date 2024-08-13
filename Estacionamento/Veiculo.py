from datetime import datetime, timedelta

class Veiculo:
    def __init__(self, placa, tipo):
        self.placa = placa
        self.tipo = tipo
        self.hora_entrada = datetime.now()
        self.gratuito = False

    def calcular_tempo_permanencia(self):
        return (datetime.now() - self.hora_entrada).total_seconds() / 60

    def __str__(self):
        return f"Veículo {self.tipo} - Placa: {self.placa}"