class model:
    """ data model class"""
    def __init__(self):
        self.directory = [
            {"firstname":'Ahmed', "familyname":'Mahdi', 'tel':'0778787887'},
            {"firstname":'Mohamed', "familyname":'Mahdi','tel':'0778787887'},
            {"firstname":'Mounir', "familyname":'Katibi','tel':'0778787887'},
            {"firstname":'Noui', "familyname":'Brahimi','tel':'0778787887'},
        ]

    def search(self, nom):
        """ lookup for a tel by lastname"""
        persons = []
        for persn in self.directory:
            if persn["familyname"] == nom:
                persons.append(persn)
        return persons

    def get_all(self):
        """ Return all people"""
        persons = []
        for persn in self.directory:
            persons.append(persn)
        return persons
class view:
    def __init__(self):
        pass
    def input(self):
        """ retrieve the name to search for"""
        print("Finding a phone")
        name = input("Give a name: ")
        return name
    
    def output(self, persons):
        """ display information from a list of persons"""
        print("List of found names")
        print(" %d found people " % len(persons))
        for pers in persons:
            print(pers["familyname"], pers["firstname"], pers['tel'])

    def output_all(self, persons):
        """ display all people in the directory"""
        print("\nAll people in the directory:")
        for pers in persons:
            print(pers["familyname"], pers["firstname"], pers['tel'])

class Controller:
    def __init__(self):
        """ controller constructor """
        self.data_model = model()  # initialisation du modèle
        self.viewer = view()       # initialisation de la vue

    def search(self):
        """ search a name """
        name = self.viewer.input()
        persons = self.data_model.search(name)
        self.viewer.output(persons)

    def display_all(self):
        """ display all people """
        persons = self.data_model.get_all()
        self.viewer.output_all(persons)

if __name__ == '__main__':
    contro = Controller()
    
    while True:
        print("\nMenu:")
        print("1. Search by family name")
        print("2. Display all people")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            contro.search()
        elif choice == '2':
            contro.display_all()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
