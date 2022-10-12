class MyOpen:
    def __init__(self, file_name, mode='r+'):
        self.file_object = open(file_name, mode)
        self.mode = mode

    def __enter__(self):
        return self.file_object

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_object.close()
        return True
