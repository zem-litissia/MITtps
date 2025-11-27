class Singleton(object):
    instance = None  # static attribute of the class

    def __new__(cls):
        """Standard Python construction method"""
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

# Use
monSingleton1 = Singleton()
monSingleton2 = Singleton()

# monSingleton1 and monSingleton2 return the same instance
assert monSingleton1 is monSingleton2

print(monSingleton1, monSingleton2)
