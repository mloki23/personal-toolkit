import os
import shutil

def organize_files(directory):
    """
    Organizes files in a directory by moving them into subdirectories based on their file extension.
    """
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = filename.split('.')[-1]
            if file_extension != '':
                destination_dir = os.path.join(directory, file_extension)
                if not os.path.exists(destination_dir):
                    os.makedirs(destination_dir)
                shutil.move(os.path.join(directory, filename), os.path.join(destination_dir, filename))