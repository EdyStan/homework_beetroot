import os

mother_folder = r'main directory path'

for folder_name in os.listdir(mother_folder):
    folder_path = mother_folder + folder_name

    for file_name in os.listdir(folder_path):
        os.rename(os.path.join(mother_folder + folder_name + '/', file_name), os.path.join(mother_folder + folder_name + '/', file_name.replace(" ", "_")))
