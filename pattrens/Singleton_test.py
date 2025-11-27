import threading

class Singleton:
    _max_access = 2
    _semaphore = threading.Semaphore(_max_access)

    def __init__(self, filename):
        self._file = open(filename, "a")

    def write(self, text):
        with self._semaphore:
            self._file.write(text + "\n")

    def close(self):
        self._file.close()



fileA = Singleton("test.txt")
fileB = Singleton("test.txt")

def write_text(file, text):
    file.write(text)

t1 = threading.Thread(target=write_text, args=(fileA, "Line 1"))
t2 = threading.Thread(target=write_text, args=(fileB, "Line 2"))

t1.start()
t2.start()
t1.join()
t2.join()

fileA.close()





