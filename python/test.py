import os

#setupFilePath = f"{os.environ['MAYA_APP_DIR']}/{}"

for name, path in os.environ.items():
    if 'MAYA' in name:
        print(name, path)