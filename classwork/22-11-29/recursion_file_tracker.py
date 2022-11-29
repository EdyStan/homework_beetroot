import os

mother_folder = r'your path'


def recursive_file_printer(the_path):
    for folder_name in os.listdir(the_path):
        print(folder_name)
        if os.path.isdir(os.path.join(the_path, folder_name)):
            recursive_file_printer(os.path.join(the_path, folder_name))

        # folder_path = the_path + folder_name
        #
        # for file_name in os.listdir(folder_path):


recursive_file_printer(mother_folder)
