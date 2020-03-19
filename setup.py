import os

path = '/private/var/mobile/Containers/Shared/AppGroup/CC849E56-88FE-4C4A-93D9-A62A38FB2B80/Pythonista3/Documents/display/display'

os.chdir(path)

init_text = open('__init__.py', 'r').read()

path = '/private/var/mobile/Containers/Shared/AppGroup/CC849E56-88FE-4C4A-93D9-A62A38FB2B80/Pythonista3/Documents/site-packages/display/'

os.mkdir(path)
os.chdir(path)

file = open('__init__.py', 'w')
file.write(init_text)
file.close()
