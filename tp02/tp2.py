# ==========================================
# AcademicElement (given by professor)
# ==========================================
from abc import abstractmethod

class AcademicElement:
    """Abstract base class for academic entities (Module, Unit, Semester, etc.)."""

    def __init__(self, name, title):
        self.name = name
        self.title = title
        self._WEEKS = 15  # Encapsulation: private attribute
        self.coef = 0
        self.credit = 0

        # Workload distribution (volume horaire)
        self.hours_lecture = 0
        self.hours_td = 0
        self.hours_tp = 0

    @abstractmethod
    def calculate_average(self):
        """Abstract method to be implemented by subclasses."""
        pass

    @abstractmethod
    def calculate_credits(self):
        """Abstract method to be implemented by subclasses."""
        pass


# ==========================================
# Module class (given by professor)
# ==========================================
class Module(AcademicElement):
    """
    Represents a teaching module with pedagogical and evaluation attributes.
    """

    def __init__(
        self,
        name: str = "",
        title: str = "",
        coef: int = 1,
        credit: int = 1,
        hours_lecture: float = 1.5,
        hours_td: float = 0,
        hours_tp: float = 0,
        teaching_mode: str = "In-person",  # "Distance" or "In-person"
        continous_percent: int = 40,
        exam_percent: int = 60
    ):
        super().__init__(name, title)
        self.coef = coef
        self.credit = credit

        # Workload distribution
        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp

        # Teaching and evaluation mode
        self.teaching_mode = teaching_mode
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent

        # Total hours x semester
        self.total_hours = self._WEEKS * (self.hours_lecture + self.hours_td + self.hours_tp)

        # Grades
        self._grades = {"tp": 0, "td": 0, "exam": 0}

    def set_grade(self, tp=None, td=None, exam=None):
        if tp is not None:
            self._grades["tp"] = tp
        if td is not None:
            self._grades["td"] = td
        if exam is not None:
            self._grades["exam"] = exam

    def calculate_average(self):
        """Polymorphism: different modules could override this behavior."""
        tp = self._grades["tp"]
        td = self._grades["td"]
        exam = self._grades["exam"]
        percent_exam = self.evaluation_exam_percent
        percent_tp = percent_td = 0

        if self.hours_tp and self.hours_td:  # not null
            percent_tp = percent_td = self.evaluation_continous_percent / 2
        elif self.hours_td:
            percent_td = self.evaluation_continous_percent
        elif self.hours_tp:
            percent_tp = self.evaluation_continous_percent

        return (
            tp * percent_tp / 100 +
            td * percent_td / 100 +
            exam * percent_exam / 100
        )

    def calculate_credits(self):
        avg = self.calculate_average()
        if avg >= 10:
            return self.credit
        else:
            return 0

    def summary(self):
        """Return a short textual description of the module."""
        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}, Credits: {self.credit}\n"
            f"Hours: total {self.total_hours}, {self.hours_lecture} Lecture, {self.hours_td} TD, {self.hours_tp} TP\n"
            f"Teaching mode: {self.teaching_mode}, "
            f"Evaluation mode: Continuous {self.evaluation_continous_percent}%, Exam {self.evaluation_exam_percent}%"
        )


# ==========================================
# Unit class (given by professor)
# ==========================================
class Unit(AcademicElement):
    """Represents a teaching unit containing multiple modules."""

    def __init__(self, name, title, modules=[]):
        super().__init__(name, title)
        self._modules = modules

    def add_module(self, module):
        self._modules.append(module)

    def calculate_average(self):
        """Example of aggregation — combining module averages."""
        if not self._modules:
            return 0
        total = sum(m.calculate_average() * m.coef for m in self._modules)
        coef_sum = sum(m.coef for m in self._modules)
        return total / coef_sum

    def calculate_credits(self):
        """Polymorphism: different modules could override this behavior."""
        if not self._modules:
            return 0
        avg = self.calculate_average()
        if avg >= 10:
            total_credits = sum(m.credit for m in self._modules)
        else:
            total_credits = sum(m.calculate_credits() for m in self._modules)
        return total_credits


# ==========================================
# Semester class (added by student)
# ==========================================
class Semester(AcademicElement):
    """Represents a semester containing multiple units."""

    def __init__(self, name, title, units=[]):
        super().__init__(name, title)
        self._units = units

    def add_unit(self, unit):
        self._units.append(unit)

    def calculate_average(self):
        """Aggregation: combining unit averages."""
        if not self._units:
            return 0
        total = sum(u.calculate_average() * sum(m.coef for m in u._modules) for u in self._units)
        coef_sum = sum(sum(m.coef for m in u._modules) for u in self._units)
        return total / coef_sum

    def calculate_credits(self):
        """Sum of all credits earned from units."""
        if not self._units:
            return 0
        return sum(u.calculate_credits() for u in self._units)


# ==========================================
# GSI Canvas – Example Usage (Step 12)
# ==========================================
if __name__ == "__main__":
    # ===== SEMESTRE 1 =====
    # UE Fondamentales
    F111 = Module("F111", "Réseaux des couches basses", coef=3, credit=6, hours_td=1.5, hours_tp=1.5)
    F112 = Module("F112", "Algorithmique Avancée et Complexité", coef=2, credit=4, hours_td=1.5, hours_tp=1.5)
    F111.set_grade(td=13, tp=14, exam=15)
    F112.set_grade(td=12, tp=13, exam=14)
    UEF11 = Unit("UEF11", "UE Fondamentales", [F111, F112])

    F121 = Module("F121", "Système d’exploitation", coef=2, credit=4, hours_td=1.5, hours_tp=1.5)
    F122 = Module("F122", "Architectures Modernes des Systèmes Informatiques", coef=2, credit=4, hours_td=1.5, hours_tp=1.5)
    F121.set_grade(td=13, tp=14, exam=13)
    F122.set_grade(td=14, tp=15, exam=15)
    UEF12 = Unit("UEF12", "UE Systèmes Informatiques", [F121, F122])

    # UE Méthodologie
    M111 = Module("M111", "Architecture et Administration des Bases de Données", coef=2, credit=4, hours_td=1.5, hours_tp=1.5)
    M112 = Module("M112", "Méthodes et Technologies d’Implémentation", coef=3, credit=5, hours_td=1.5, hours_tp=1.5)
    M111.set_grade(td=12, tp=13, exam=14)
    M112.set_grade(td=13, tp=13, exam=15)
    UEM11 = Unit("UEM11", "UE Méthodologie", [M111, M112])

    # UE Découverte
    D111 = Module("D111", "Systèmes de Communication Vocaux et Vidéos", coef=2, credit=2, hours_td=1.5, hours_tp=1.5)
    D111.set_grade(td=12, tp=12, exam=13)
    UED11 = Unit("UED11", "UE Découverte", [D111])

    # UE Transversale
    T111 = Module("T111", "Cloud Computing", coef=1, credit=1, hours_td=1.5)
    T111.set_grade(td=15, exam=15)
    UET11 = Unit("UET11", "UE Transversale", [T111])

    # Assemblage Semestre 1
    S1 = Semester("S1", "Semestre 1", [UEF11, UEF12, UEM11, UED11, UET11])

    print("=== SEMESTRE 1 ===")
    print("Average:", round(S1.calculate_average(), 2))
    print("Credits:", S1.calculate_credits())

    # ===== SEMESTRE 2 =====
    F211 = Module("F211", "Middleware pour les systèmes répartis", coef=3, credit=6, hours_td=1.5, hours_tp=1.5)
    F212 = Module("F212", "Modélisation et Architectures Logicielles", coef=2, credit=4, hours_td=1.5, hours_tp=1.5)
    F211.set_grade(td=13, tp=13, exam=15)
    F212.set_grade(td=14, tp=13, exam=14)
    UEF21 = Unit("UEF21", "UE Fondamentales 2", [F211, F212])

    F221 = Module("F221", "Réseaux de la couche IP", coef=3, credit=6, hours_td=1.5, hours_tp=1.5)
    F222 = Module("F222", "Introduction au Machine Learning", coef=2, credit=4, hours_td=1.5, hours_tp=1.5)
    F221.set_grade(td=13, tp=13, exam=14)
    F222.set_grade(td=14, tp=14, exam=15)
    UEF22 = Unit("UEF22", "UE Réseaux et IA", [F221, F222])

    M211 = Module("M211", "Infographie", coef=2, credit=3, hours_td=1.5, hours_tp=1.5)
    M212 = Module("M212", "Gestion de l’incertain", coef=2, credit=3, hours_td=1.5, hours_tp=1.5)
    M211.set_grade(td=13, tp=14, exam=15)
    M212.set_grade(td=12, tp=13, exam=14)
    UEM21 = Unit("UEM21", "UE Méthodologique", [M211, M212])

    D211 = Module("D211", "Internet of Things", coef=2, credit=3, hours_td=1.5, hours_tp=1.5)
    D211.set_grade(td=13, tp=13, exam=14)
    UED21 = Unit("UED21", "UE Découverte", [D211])

    T211 = Module("T211", "Cybercriminalité", coef=1, credit=1, hours_td=1.5)
    T211.set_grade(td=15, exam=15)
    UET21 = Unit("UET21", "UE Transversale", [T211])

    # Assemblage Semestre 2
    S2 = Semester("S2", "Semestre 2", [UEF21, UEF22, UEM21, UED21, UET21])

    print("\n=== SEMESTRE 2 ===")
    print("Average:", round(S2.calculate_average(), 2))
    print("Credits:", S2.calculate_credits())

    # ===== Année complète =====
    year_average = (S1.calculate_average() + S2.calculate_average()) / 2
    total_credits = S1.calculate_credits() + S2.calculate_credits()
    print("\n=== Résumé Annuel ===")
    print("Year Average:", round(year_average, 2))
    print("Total Credits:", total_credits)
