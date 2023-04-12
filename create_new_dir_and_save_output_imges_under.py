import shutil
import os

parent_directory = "./TextToImage/"

all_images = []

def send_images_under_new_created_folder(parent_directory, new_directory):

    for file in os.listdir(parent_directory):
        f_name, f_ext = os.path.splitext(file)
        if file.endswith(".png"):
            all_images.append(file)
        else:
            pass

    __create_new_folder(parent_directory, new_directory)

    for filename in all_images:
        shutil.move(os.path.join(parent_directory, filename), new_directory)

    
def __create_new_folder(parent_directory, new_directory):
    new_path = os.path.join(parent_directory, new_directory)
    if os.path.exists(new_path):
        print('\n[INFO]>>> Path already exists\n')
    else:
        print('\n[INFO]>>> New path created\n')
        os.mkdir(new_path)


def clear_main_route(parent_directory):
    for file in os.listdir(parent_directory):
        f_name, f_ext = os.path.splitext(file)
        if file.endswith(".png"):
            all_images.append(file)
        else:
            pass


def find_dir_name(parent_directory):
    for file in os.listdir(parent_directory):
        f_name, f_ext = os.path.splitext(file)
        if file.endswith("zoom.png"):
            f_name =f_name.split("-")[2]
        
            return f_name

