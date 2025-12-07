class RealSubject:
    """
    The RealSubject contains some core business logic. Usually, RealSubjects are
    capable of doing some useful work which may also be very slow or sensitive
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the RealSubject's code.
    """
    def request(self):
        print("RealSubject: Handling request.")


class Proxy(RealSubject):
    """
    The Proxy has an interface identical to the RealSubject.
    """
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling access, logging, etc. The Proxy can perform one
        of these tasks and then call the RealSubject if allowed.
        """
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access before sending the real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of the request.")


def client_code(subject: RealSubject):
        """
        The client works with both RealSubject and Proxy using the same interface.
        """
        subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\nClient: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
