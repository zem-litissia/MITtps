class model_file:
    """ Data Model class that stores information in a text file """
    
    def __init__(self):
        self.directory = []
        try:
            myfile = open("directory.txt", "r")
        except:
            print("Can't open DataFile")
        
        lines = myfile.readlines()
        for line in lines:
            line = line.strip('\n')
            fields = line.split('\t')
            if len(fields) >= 3:
                person = {}
                person["familyname"] = fields[0]
                person["firstname"] = fields[1]  # corrige la faute "lastname"
                person["tel"] = fields[2]
                self.directory.append(person)
        myfile.close()
    
    def __del__(self):
        """ Destructor: save all data to the file at the end of the program """
        try:
            myfile = open("directory.txt", "w")
        except:
            print("Can't open DataFile")
            sys.exit()
        
        for person in self.directory:
            line = "\t".join([person['familyname'],
                              person['firstname'],
                              person['tel']])
            line += "\n"
            myfile.write(line)
        myfile.close()
      
    def search(self, name):
        """Search people by family name"""
        persons = []
        for pers in self.directory:
            if pers["familyname"] == name:
                persons.append(pers)
        return persons
    
    def get_all(self):
        """Return all people"""
        return self.directory.copy()
    
    def add(self, name, firstname, tel):
        """Add a new person"""
        person = {}
        person["familyname"] = name
        person["firstname"] = firstname
        person["tel"] = tel
        self.directory.append(person)

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
    def input_add(self):
        """Get info to add a new person"""
        print("Add a person")
        print("Give a name")
        name = input()
        print("Give a first name")
        firstname = input()
        print("Give a telephone number")
        tel = input()
        return (name, firstname, tel)
class Controller:
    def __init__(self):
        """ controller constructor """
        self.data_model = model_file()  # initialisation du modèle
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
    def add(self):
        """Add a new person"""
        name, firstname, tel = self.viewer.input_add()
        self.data_model.add(name, firstname, tel)
        persons = self.data_model.get_all()
        self.viewer.output(persons)
if __name__ == '__main__':
    contro = Controller()
    
    while True:
        print("\nMenu:")
        print("1. Search by family name")
        print("2. Display all people")
        print("3. Add a new person")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            contro.search()
        elif choice == '2':
            contro.display_all()
        elif choice == '3':
            contro.add()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
