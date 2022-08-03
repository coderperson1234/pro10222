import os 
import shutil 
fromDirectory = '/Users/aaravshah/Downloads/C102_assets-main'
toDirectory = '/Users/aaravshah/Desktop/Classes/CODING/PYTHON/C102Images'
directories = os.listdir(fromDirectory)
# print(directories)
for fileName in directories:
    location, extension = os.path.splitext(fileName)
   #  print(location)
   #  print(extension)
    if extension =='':
        continue
    if extension in ['.gif', '.png', '.jpg','.jfif', '.jpeg','.bmp']:
        path1 = fromDirectory + '/' + fileName
        path2 = toDirectory + '/' + "C102Images"
        path3 = toDirectory +'/' + "C102Images" + "/" + fileName
        print(path1)
        print(path3)
        if os.path.exists(path2):
             print("Moving " + fileName + ".....")
             shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            print("Moving " + fileName + ".....")
            shutil.move(path1, path3)
             