import shutil
import os
import zipfile

from datetime import datetime


def backup_folder(source, destination):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_path = os.path.join(
        destination,
        f"backup_{timestamp}"
    )

    shutil.copytree(source, backup_path)

    return backup_path


def compress_folder(folder_path):

    zip_path = folder_path + ".zip"

    with zipfile.ZipFile(zip_path, 'w') as z:

        for root, dirs, files in os.walk(folder_path):

            for file in files:

                file_path = os.path.join(root, file)

                z.write(file_path)

    return zip_path


def restore_backup(zip_file, extract_to):

    with zipfile.ZipFile(zip_file, 'r') as z:

        z.extractall(extract_to)

    return "Backup Restored Successfully"
