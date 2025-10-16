class NutritionTracker:
    def __init__(self):
        self.meals = []

    def add_meal(self):
        refeicao = input("Digite a refeição (ex: café da manhã, almoço): ")
        descricao = input("Descreva o que comeu: ")
        self.meals.append((refeicao, descricao))
        print("🍎 Refeição registrada com sucesso!")

    def show_summary(self):
        print("\n🥗 Alimentação:")
        if not self.meals:
            print("Nenhuma refeição registrada ainda.")
        else:
            for i, (refeicao, descricao) in enumerate(self.meals, 1):
                print(f"{i}. {refeicao.capitalize()}: {descricao}")
