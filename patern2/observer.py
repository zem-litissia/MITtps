"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.
"""

class Subject:
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """
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

    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer:
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """
    def __init__(self):
        self._subject = None
        self._observer_state = None

    def update(self, arg):
        pass

    def show(self):
        print(self._observer_state)


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """
    def update(self, arg):
        self._observer_state = arg


def main():
    subject = Subject()
    ahmed_observer = ConcreteObserver()
    salem_observer = ConcreteObserver()

    subject.attach(ahmed_observer)
    subject.attach(salem_observer)

    subject.subject_state(123)
    ahmed_observer.show()
    salem_observer.show()

    subject.subject_state(99)
    ahmed_observer.show()
    salem_observer.show()
if __name__ == "__main__":
    main()
