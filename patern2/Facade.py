class Subsystem1:

    def operation1(self):
        print("operation retrait ccp")

    def operation2(self):
        print("operation virement ccp")


class Subsystem2:
    """ Implémente les fonctionnalités du sous-système.
    """
    def operation1(self):
        print("operation paiement facture de l'eau (ADE)")


class Subsystem3:
    """
    Implémente les fonctionnalités du sous-système.
    """
    def operation1(self):
        print("operation paiement facture d'électricité/gaz (Sonelgaz)")


class Facade:
    """
    Interface simplifiée qui regroupe les opérations
    des sous-systèmes.
    """
    def __init__(self):
        self._subsystem_1 = Subsystem1()
        self._subsystem_2 = Subsystem2()
        self._subsystem_3 = Subsystem3()

    def operation_retait_ccp(self):
        self._subsystem_1.operation1()

    def operation_virment_ccp(self):
        self._subsystem_1.operation2()

    def operation_fact_eau(self):
        self._subsystem_2.operation1()

    def operation_fact_elec_gaz(self):
        self._subsystem_3.operation1()


def main():
    facade = Facade()
    facade.operation_retait_ccp()
    facade.operation_virment_ccp()
    facade.operation_fact_eau()
    facade.operation_fact_elec_gaz()


if __name__ == "__main__":
    main()
