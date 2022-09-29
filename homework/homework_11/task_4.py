class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "w") as file_object:
            file_object.write(self.msg)


raise CustomException('some text\nI love my life sometimes')
