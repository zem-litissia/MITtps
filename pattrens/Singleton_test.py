import sqlite3
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_name):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._connection = sqlite3.connect(db_name)
            return cls._instance

    def execute(self, query):
        cursor = self._connection.cursor()
        cursor.execute(query)
        self._connection.commit()
        return cursor

    def close(self):
        self._connection.close()


db1 = Singleton("mydb.db")
db2 = Singleton("mydb.db")

assert db1 is db2
db1.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER)")
db1.close()
