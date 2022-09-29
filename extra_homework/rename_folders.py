import os

mother_folder = r'main directory path'

for folder_name in os.listdir(mother_folder):
    os.rename(os.path.join(mother_folder, folder_name),
              os.path.join(mother_folder, folder_name.replace(" ", "_")))
