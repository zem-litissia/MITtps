import threading

class Singleton(object):
    _instance = None
    _lock = threading.Lock() 

    def __new__(cls, filename):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._file = open(filename, "w")  
            return cls._instance

    def write(self, text):
        """Write text to the file"""
        self._file.write(text + "\n")
        self._file.flush()  

    def close(self):
        """Close the file"""
        self._file.close()
        Singleton._instance = None 



writer1 = Singleton("output.txt")
writer1.write("Hello World!")

writer2 = Singleton("output.txt")
writer2.write("This is the same file instance!")

print(writer1 is writer2) 
writer1.close()
