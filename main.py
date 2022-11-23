# Script to Extract data from the zip file.

from zipfile import ZipFile
import os


path = '~/projects/ml_ai_projects/git_first_pull/Data.zip'

file_name = str(os.path.basename(path))


with ZipFile(file_name) as zip:
    zip.extractall()

  