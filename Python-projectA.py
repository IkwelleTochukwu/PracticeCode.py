# Selective copy
# This program walks through a folder tree and searches for files with a certain
# extension (such as, .pdf, .py or .jpg). And copy these files from whatever location they
# are into a new folder.
from fileinput import filename
import os, shutil

folder = input('Enter absolute path of directory to copy from:\n')
extension = input('Enter extension to copy:\n')
destination = input('Enter destination absolute path of the folder:\n')

for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith(extension):
            shutil.copy(os.path.join(folder, filename), destination)

print('successfully copied files to ' + os.path.basename(destination))