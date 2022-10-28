class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
        with open("logs.txt", "a") as file_object:
            file_object.write(f'{self.msg}')


raise CustomException('Exception oops!\n')
