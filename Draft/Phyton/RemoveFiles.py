import os
import os.path as op


def main():
    file_path = 'y:\\English\Books\\'
    for path, subdirs, files in os.walk(file_path):
        for name in files:
            file_pathname = os.path.join(path, name)
            if 'Копировать(' in file_pathname:
                os.remove(file_pathname)
                print(file_pathname)

if __name__=='__main__':
    main()