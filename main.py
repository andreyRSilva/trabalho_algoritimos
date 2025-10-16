from user import User
from sleep import SleepTracker
from nutrition import NutritionTracker
from fitness import FitnessTracker
from medication import MedicationReminder


def main():
    print("🌿 Bem-vindo ao aplicativo Vida+ 🌿")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    user = User(nome, idade)
    
    sleep_tracker = SleepTracker()
    nutrition_tracker = NutritionTracker()
    fitness_tracker = FitnessTracker()
    medication_reminder = MedicationReminder()

    while True:
        print("\n--- Menu Principal ---")
        print("1. Registrar rotina de sono")
        print("2. Registrar alimentação")
        print("3. Registrar atividade física")
        print("4. Registrar medicamentos")
        print("5. Ver resumo diário")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            sleep_tracker.add_sleep_log()
        elif opcao == "2":
            nutrition_tracker.add_meal()
        elif opcao == "3":
            fitness_tracker.add_activity()
        elif opcao == "4":
            medication_reminder.add_medication()
        elif opcao == "5":
            print("\nResumo diário de", user.nome)
            sleep_tracker.show_summary()
            nutrition_tracker.show_summary()
            fitness_tracker.show_summary()
            medication_reminder.show_summary()
        elif opcao == "0":
            print("Saindo... até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
