import os

mother_folder = r'/home/edystan/Desktop/folderul_D/courses/beetroot_academy'


def recursive_file_printer(the_path, the_tab=""):
    for folder_name in os.listdir(the_path):
        print(the_tab + folder_name)
        if os.path.isdir(os.path.join(the_path, folder_name)):
            next_tab = the_tab + "   "
            recursive_file_printer(os.path.join(the_path, folder_name), next_tab)

        # folder_path = the_path + folder_name
        #
        # for file_name in os.listdir(folder_path):


recursive_file_printer(mother_folder)
