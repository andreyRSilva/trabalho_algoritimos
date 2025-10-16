class MedicationReminder:
    def __init__(self):
        self.medications = []

    def add_medication(self):
        nome = input("Nome do medicamento: ")
        horario = input("Horário para tomar (ex: 08:00): ")
        instrucao = input("Instruções do médico/farmacêutico: ")
        self.medications.append((nome, horario, instrucao))
        print("💊 Medicamento registrado com sucesso!")

    def show_summary(self):
        print("\n💊 Medicamentos:")
        if not self.medications:
            print("Nenhum medicamento registrado ainda.")
        else:
            for i, (nome, horario, instrucao) in enumerate(self.medications, 1):
                print(f"{i}. {nome} - {horario} | {instrucao}")
