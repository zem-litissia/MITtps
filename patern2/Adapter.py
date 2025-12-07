class MachineDate:
    def __init__(self, date_machine):
        self.date = date_machine  # exemple : "2025/12/02"


class DateAdapter:
    def afficher(self):
        raise NotImplementedError
        

class Adapter_MM_DD_YYYY(DateAdapter):
    def __init__(self, machine_date: MachineDate):
        y, m, d = machine_date.date.split("/")
        self.result = f"{m}/{d}/{y}"

    def afficher(self):
        return self.result


class Adapter_DD_MM_YYYY(DateAdapter):
    def __init__(self, machine_date: MachineDate):
        y, m, d = machine_date.date.split("/")
        self.result = f"{d}/{m}/{y}"

    def afficher(self):
        return self.result


def main():
    d = MachineDate("2025/12/02")

    adapter1 = Adapter_MM_DD_YYYY(d)
    adapter2 = Adapter_DD_MM_YYYY(d)

    print(adapter1.afficher())  # 12/02/2025
    print(adapter2.afficher())  # 02/12/2025


if __name__ == "__main__":
    main()
