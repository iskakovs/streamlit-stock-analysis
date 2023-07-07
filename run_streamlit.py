import os #package is useful for joining information from different files (os.path.join)

# Define the Projects' main file on which you will do all the manipulations
APP_ENTRY_POINT = 'main.py'

# Define 'dir_path' as a variable for compiling all the files in one 'main' file
dir_path = os.path.dirname(__file__)
path = os.path.join(dir_path, APP_ENTRY_POINT)
os.system('streamlit run "{}"'.format(path))
