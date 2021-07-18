import os
import sys
import re
import string
import configparser

droppedFile = sys.argv[1]

with open (droppedFile) as x:
	fileList = x.readlines()
	a = 0
while a < len(fileList):
	fileList[a] = fileList[a].strip('\n')
	a += 1

newFileName = (os.path.basename(sys.argv[1]))
newFile = open(newFileName.split('.')[0] + '.txt', "w+")

def write_file():
	config.write(open('Settings.ini', 'w'))

config = configparser.RawConfigParser()
#if settings file doesn't exist create a blank one
if not os.path.exists('Settings.ini'):
	config['BlacklistedVoxels'] = {'Blacklist': ''}
	config['FSEditedVoxels'] = {'FSEdit': '' }
	write_file()

config.read(".\Settings.ini")

position = 0

while position < len(fileList):
	line = fileList[position]
	if os.path.exists(".\Settings.ini"):
		BlacklistGet = config.get('BlacklistedVoxels', 'Blacklist', fallback='')
		Blacklist = BlacklistGet.split(', ')
		FSVoxelsGet = config.get('FSEditedVoxels', 'FSEdit', fallback='')
		FSVoxels = FSVoxelsGet.split(', ')
	else:
		BlacklistGet = ("")
		Blacklist = ("")
		FSVoxelsGet = ("")
		FSVoxels = ("")

	if re.search('voxel', line, re.I):
		tilenumber = re.findall(r'\b\d+\b', line)
		
		for x in tilenumber:
			
			#For Voxels that don't work in FS
			y = int(tilenumber.index(x))
			if tilenumber[y] in Blacklist:
				blacklisted = ("// ")
			if not tilenumber[y] in Blacklist:
				blacklisted = ("")
				
			#For Voxels that need modifications for FS
			if tilenumber[y] in FSVoxels:
				FSVoxel = ("_FS")
			if not tilenumber[y] in FSVoxels:
				FSVoxel = ("")

		#For Voxels that rotate
		if ' rotate ' in line:
			Rotate = " rotate TRUE"
		else:
			Rotate = ""
			
		newline = (blacklisted + 'Voxel ' + tilenumber[0] + ' { filename ' + line.split(' ')[1].strip()[:-5] + FSVoxel + '.kvx"' + Rotate + " }" + line.split('}')[1] )
		
		fileList[position] = newline
		
		#For Voxels that have multiple tiles listed in the line (tile0 xxxx tile1 yyyy etc)
		if len(tilenumber) >= 2:
			for x in tilenumber[1:]:
				y = int(tilenumber.index(x))
				
				#For some reason having "Voxel" causes this to break
				fileList.insert(position + y, (blacklisted + 'Voxe ' + tilenumber[y] + ' { filename ' + line.split(' ')[1].strip()[:-5] + FSVoxel + '.kvx"' + Rotate + " }" + line.split('}')[1] ))

	position += 1


position = 0

if not (BlacklistGet == ("")):
	print('Blacklisted Voxels: ' + BlacklistGet)
if not (FSVoxelsGet == ("")):
	print('FS Edited Voxels: ' + FSVoxelsGet)

#Replace Voxe with Voxel
fileList = [item.replace("Voxe ", "Voxel ") for item in fileList]
	
position = 0

#write everything to file
while position < len(fileList):
	newFile.write(fileList[position] + "\n")
	position += 1