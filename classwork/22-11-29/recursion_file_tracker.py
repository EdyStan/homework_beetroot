import os


def recursive_file_printer(the_path, the_tab=""):
    for folder_name in os.listdir(the_path):
        print(the_tab + folder_name)
        if os.path.isdir(os.path.join(the_path, folder_name)):
            next_tab = the_tab + "   "
            recursive_file_printer(os.path.join(the_path, folder_name), next_tab)


mother_folder = r'<type pwd in your terminal and paste here>'

recursive_file_printer(mother_folder)
