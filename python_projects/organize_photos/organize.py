import os
import glob

origin = '/Users/lcosta5/Downloads/'
destiny = '/Users/lcosta5/Google\ Drive/'

command = 'mv %s %s'

def move_files(list, folder):
    file = None
    path_folder = destiny + folder
    for file in list:
        if 'important' in file:
            try:
                os.system((command % (file, path_folder)))
            except Exception as e:
                file = open('error.txt', 'w+')
                file.write('Error : %s ' % (e))
            finally:
            	if file is None:
            		break
            	else : 
            		file.close()


def main():
    photos_jpg = glob.glob(origin + '*.jpg')
    photos_png = glob.glob(origin + '*.png')

    path_fotos =  'Multimidia/Fotos/autobackup/'

    move_files(photos_jpg, path_fotos)
    move_files(photos_png, path_fotos)


if '__main__' == __name__ :
    main()