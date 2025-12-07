# Strategy pattern applied to a bank credit procedure

class CreditContext:
    """
    Maintains a reference to a CreditStrategy object.
    """
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        """
        Allows changing the strategy at runtime.
        """
        self._strategy = strategy

    def calculate_credit(self, amount):
        return self._strategy.calculate(amount)


class CreditStrategy:
    """
    Strategy interface for credit calculation.
    """
    def calculate(self, amount):
        raise NotImplementedError("This method should be overridden.")


class CreditWithInterest(CreditStrategy):
    """
    Concrete strategy for credit with interest.
    """
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate

    def calculate(self, amount):
        return amount + (amount * self.interest_rate / 100)


class CreditWithoutInterest(CreditStrategy):
    """
    Concrete strategy for credit without interest.
    """
    def calculate(self, amount):
        return amount


# Example usage
def main():
    amount = 1000

    # Credit with interest
    credit_with_interest = CreditWithInterest(5)  # 5% interest
    context = CreditContext(credit_with_interest)
    print("Credit with interest:", context.calculate_credit(amount))

    # Credit without interest
    credit_without_interest = CreditWithoutInterest()
    context.set_strategy(credit_without_interest)
    print("Credit without interest:", context.calculate_credit(amount))


if __name__ == "__main__":
    main()
