# ==========================================
# Semester class
# ==========================================
from AcademicElement import AcademicElement

class Semester(AcademicElement):
    """Represents a semester containing multiple units."""

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self._units = units if units else []

    def add_unit(self, unit):
        self._units.append(unit)

    def calculate_average(self):
        if not self._units:
            return 0
        total = sum(u.calculate_average() * sum(m.coef for m in u._modules) for u in self._units)
        coef_sum = sum(sum(m.coef for m in u._modules) for u in self._units)
        return total / coef_sum

    def calculate_credits(self):
        if not self._units:
            return 0
        return sum(u.calculate_credits() for u in self._units)
