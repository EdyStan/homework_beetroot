import sqlite3


class ContextManagerSQL:

    def __init__(self, file_name):
        self.file_obj = sqlite3.connect(file_name)

    def __enter__(self):
        return self.file_obj.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
