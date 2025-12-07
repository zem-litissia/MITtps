# Observer pattern applied to notifications

class Subject:
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    def new_post(self, post):
        self._subject_state = post
        self._notify()


class Observer:
    def __init__(self):
        self._subject = None
        self._observer_state = None

    def update(self, arg):
        pass

    def show(self):
        print(self._observer_state)


class StudentObserver(Observer):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def update(self, post):
        self._observer_state = f"{self.name} received notification: {post}"


# Example usage
def main_notifications():
    department_site = Subject()

    ahmed = StudentObserver("Ahmed")
    salem = StudentObserver("Salem")

    department_site.attach(ahmed)
    department_site.attach(salem)

    department_site.new_post("New assignment uploaded!")
    ahmed.show()
    salem.show()

    department_site.new_post("Exam schedule released!")
    ahmed.show()
    salem.show()


if __name__ == "__main__":
    main_notifications()
