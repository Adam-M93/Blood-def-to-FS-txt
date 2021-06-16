import os
import sys
import re
import string


droppedFile = sys.argv[1]

#x = open(droppedFile)
with open (droppedFile) as x:
    fileList = x.readlines()
    a = 0
while a < len(fileList):
    fileList[a] = fileList[a].strip('\n')
    a += 1

newFileName = (os.path.basename(sys.argv[1]))
newFile = open(newFileName.split('.')[0] + '.txt', "w+")



position = 0

while position < len(fileList):
    line = fileList[position]

    if re.search('voxel', line, re.I):
        if re.search('rotate', line, re.I):
            tilenumber = line[line.find('e ')+1:line.find(' r')]
            newline = ('Voxel' + tilenumber + ' { filename ' + line.split(' ')[1].strip() + " rotate TRUE }" )
        else:
            tilenumber = line[line.find('e ')+1:line.find(' }')]
            newline = ('Voxel' + tilenumber + ' { filename ' + line.split(' ')[1].strip() + " }" )
        fileList[position] = newline
    
    position += 1


position = 0
#write everything to file
while position < len(fileList):
    newFile.write(fileList[position] + "\n")
    position += 1


os.system("pause")
