# UZH PCL1 HS2022
# Script for checking everything necessary is installed
# By Eyal Dolev (PfL tutor team HS2021)
# Modded by Alison Kim (PfL tutor team HS2022)

import platform
import sys


print(f'You are running Python version {platform.python_version()}.\n')

# Ensure the right version of Python is running.
if sys.version_info.major < 3:
    print('You need Python 3. Try running this script again with "python3".')
    exit(1)
elif sys.version_info.minor < 10:
    print('Your Python 3 version is too old. Please update to Python 3.10.x by downloading the installer directly from https://www.python.org/downloads/.')
    exit(1)
else:
    print(f'Python version is up-to-date.\n')


# Ensure all necessary modules are installed.
errors = []
try:
    import nltk
    try:
        nltk.download('book')
    except:
        errors.append('nltk corpus: \'book\'')
    
    try:
        nltk.app.chunkparser()
    except:
        errors.append('nltk attribute: \'chunkparser\'')
except:
    errors.append('nltk')

if errors:
    print('The following modules/files are missing:')
    for error in errors:
        print(f'\t* {error}')
else:
    print("You have successfully installed everything! Congratulations!")