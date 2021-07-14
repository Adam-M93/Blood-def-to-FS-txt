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
		tilenumber = line[line.find('e ')+1:line.find(' r')].strip()
		
		#For Voxels that don't work in FS
		if tilenumber in Blacklist:
			blacklisted = ("\\\ ")
		if not tilenumber in Blacklist:
			blacklisted = ("")

		#For Voxels that need modifications for FS
		if tilenumber in FSVoxels:
			FSVoxel = ("_FS")
		if not tilenumber in FSVoxels:
			FSVoxel = ("")
			
		if re.search('rotate', line, re.I):
			newline = (blacklisted + 'Voxel ' + tilenumber + ' { filename ' + line.split(' ')[1].strip()[:-5] + FSVoxel + ".kvx" + " rotate TRUE }" )
		else:
			newline = (blacklisted + 'Voxel ' + tilenumber + ' { filename ' + line.split(' ')[1].strip()[:-5] + FSVoxel + ".kvx" + " }" )

		fileList[position] = newline
		
	position += 1


position = 0

if not (BlacklistGet == ("")):
	print('Blacklisted Voxels: ' + BlacklistGet)
if not (FSVoxelsGet == ("")):
	print('FS Edited Voxels: ' + FSVoxelsGet)
	
#write everything to file
while position < len(fileList):
	newFile.write(fileList[position] + "\n")
	position += 1