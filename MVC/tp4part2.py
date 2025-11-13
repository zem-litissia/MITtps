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
        # found people list
        persons = []
        for persn in self.directory:
        # show all people with the given name
            if persn["familyname"] == nom:
                 persons.append(persn)
            # return a list of dictionaries
        return persons
     def get_all(self):
        """ Find a tel by name"""
        # List of found people
        persons = []
        for persn in self.directory:
        # display all people
             persons.append(persn)
        # a table with field names
        return persons
class view:
    def __init__(self,):
        pass

    def input(self,):
        """ retrieve the name to search for"""
        print("Finding a phone")
        print("Give a name")
        name = input()
        return name

    def output(self, persons):
        """ display information from a list of persons"""
        print("List of found names")
        print(" %d found people "%len(persons))
        for pers in persons:
             print(pers["familyname"], pers["firstname"], pers['tel'])
             
    def output_all(self, persons):
        """ display all people in the directory"""
        print("\nAll people in the directory:")
        for pers in persons:
             print(pers["familyname"], pers["firstname"], pers['tel'])

def controller():
    data_model = model()
    myviewer = view()

    while True:
        print("\nMenu:")
        print("1. Search by family name")
        print("2. Display all people")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = myviewer.input()
            persons = data_model.search(name)
            myviewer.output(persons)
        elif choice == '2':
            persons = data_model.get_all()
            myviewer.output_all(persons)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")
          
if __name__ == '__main__':
        controller()