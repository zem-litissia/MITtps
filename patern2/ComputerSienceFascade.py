class InfoFacade:
    def __init__(self):
        self._dep_site = DepartmentWebsite()
        self._info_platform = ELearningInfo()
        self._univ_platform = UniversityELearning()
        self._facebook_pages = FacebookPages()
        self._student_groups = StudentGroups()

    def show_all_resources(self):
        self._dep_site.show()
        self._info_platform.show()
        self._univ_platform.show()
        self._facebook_pages.show()
        self._student_groups.show()


class DepartmentWebsite:
    def show(self):
        print("Affichage du site du département")


class ELearningInfo:
    def show(self):
        print("Affichage de la plateforme e-learning Info")


class UniversityELearning:
    def show(self):
        print("Affichage de la plateforme e-learning de l'université")


class FacebookPages:
    def show(self):
        print("Affichage des pages Facebook du département, faculté et université")


class StudentGroups:
    def show(self):
        print("Affichage des groupes étudiants")


def main():
    facade = InfoFacade()
    facade.show_all_resources()


if __name__ == "__main__":
    main()