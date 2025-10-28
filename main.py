# ==========================================
# GSI Project — Example Usage
# ==========================================
from module import Module
from unit import Unit
from semester import Semester

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
