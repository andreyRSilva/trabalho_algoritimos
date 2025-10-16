class SleepTracker:
    def __init__(self):
        self.sleep_logs = []

    def add_sleep_log(self):
        hora_dormir = input("Hora que você dormiu (ex: 22:30): ")
        hora_acordar = input("Hora que você acordou (ex: 06:30): ")
        self.sleep_logs.append((hora_dormir, hora_acordar))
        print("💤 Rotina de sono registrada com sucesso!")

    def show_summary(self):
        print("\n📘 Qualidade do Sono:")
        if not self.sleep_logs:
            print("Nenhum registro de sono ainda.")
        else:
            for i, log in enumerate(self.sleep_logs, 1):
                print(f"{i}. Dormiu às {log[0]} e acordou às {log[1]}")
