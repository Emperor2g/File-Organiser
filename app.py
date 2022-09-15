import os
import shutil

SOURCE_DIR = input("Enter the location of where you want to move your files from: ")
DESTINATION_DIR = input("Enter the location of where you want to move your files to: ")

verifyFolder = ["", "Folders", "Programmes", "Compressed", "Documents", "Images", "Videos", "Misc"]


def transferfile(source, is_dir, folderval):
    shutil.move(source, os.path.join(DESTINATION_DIR, verifyFolder[folderval]))
    if is_dir:
        print("Folder has been moved to" + DESTINATION_DIR + verifyFolder[folderval])
    else:
        print("File has been moved to" + DESTINATION_DIR + verifyFolder[folderval])


for v in verifyFolder:
    if not os.path.exists(os.path.join(DESTINATION_DIR, v)):
        os.mkdir(os.path.join(DESTINATION_DIR, v))
        print("Created folder" + v)

for files in os.listdir(SOURCE_DIR):
    if os.path.isdir((os.path.join(SOURCE_DIR, files))):
        transferfile(os.path.join(SOURCE_DIR, files), True, 1)
    elif files.endswith(('.exe', '.pkg', '.msi')):
        transferfile(os.path.join(SOURCE_DIR, files), False, 2)
    elif files.endswith(('.zip', '.rar')):
        transferfile(os.path.join(SOURCE_DIR, files), False, 3)
    elif files.endswith(('.doc', '.docx', '.pdf', '.json')):
        transferfile(os.path.join(SOURCE_DIR, files), False, 4)
    elif files.endswith(('.tif', '.tiff', '.jpg', '.jpeg', '.gif', '.png')):
        transferfile(os.path.join(SOURCE_DIR, files), False, 5)
    elif files.endswith(('.mp4', '.mov')):
        transferfile(os.path.join(SOURCE_DIR, files), False, 6)
    else:
        transferfile(os.path.join(SOURCE_DIR, files), False, 7)

print('Completed!!!')