# ==========================================
# Module class
# ==========================================
from AcademicElement import AcademicElement



class Module(AcademicElement):
    """Represents a teaching module with pedagogical and evaluation attributes."""

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
        tp = self._grades["tp"]
        td = self._grades["td"]
        exam = self._grades["exam"]
        percent_exam = self.evaluation_exam_percent
        percent_tp = percent_td = 0

        if self.hours_tp and self.hours_td:
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
        return self.credit if avg >= 10 else 0

    def summary(self):
        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}, Credits: {self.credit}\n"
            f"Hours: total {self.total_hours}, {self.hours_lecture} Lecture, {self.hours_td} TD, {self.hours_tp} TP\n"
            f"Teaching mode: {self.teaching_mode}, "
            f"Evaluation: Continuous {self.evaluation_continous_percent}%, Exam {self.evaluation_exam_percent}%"
        )
