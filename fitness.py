class FitnessTracker:
    def __init__(self):
        self.activities = []

    def add_activity(self):
        tipo = input("Tipo de exercício (ex: caminhada, musculação): ")
        duracao = input("Duração (em minutos): ")
        self.activities.append((tipo, duracao))
        print("🏋️ Atividade física registrada com sucesso!")

    def show_summary(self):
        print("\n💪 Atividades Físicas:")
        if not self.activities:
            print("Nenhuma atividade registrada ainda.")
        else:
            for i, (tipo, duracao) in enumerate(self.activities, 1):
                print(f"{i}. {tipo.capitalize()} - {duracao} min")
