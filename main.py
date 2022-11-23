# Script to Extract data from the zip file.

from zipfile import ZipFile
import os


path = '~/projects/ml_ai_projects/git_first_pull/Dataset/archive.zip'

file_name = str(os.path.basename(path))


with ZipFile('./Dataset/archive.zip') as zip:
    zip.extractall()

  