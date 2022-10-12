from task_1_class import MyOpen

with MyOpen('text_test.txt', 'a+') as file_obj:
    file_obj.write('Look! There\'s text!\n')
    file_obj.close()

with MyOpen('text_test.txt', 'r+') as file_obj:
    load = file_obj.read()
    print(load)
    file_obj.close()
