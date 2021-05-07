# -*- coding: utf-8 -*-

"""

	Step 1: Change the filename to increasing number and save
their map, for opencv do not support file path beyond ASCII.

	This version is for changing names at the first time, for
some images in different tasks in the dataset share the same
name and some do not. The situation, some images exist at the
second task while not appear before, should be considered 
independently.

	Every task has a unique folder map, and all tasks share
the same filename map.

"""

import os.path
import json

folder_name = "xiangLinYaGenJianWeiZhi_12_O" # your data folder's name
work_dir = ".\\" + folder_name # direction of your data
fileType = '.tif' # your data type

# count all unique image, that means if an image was marked as
# more than one class, its name after changed will be the same
img_count = 0

# the map aims to ease the process, is not for training
filename_map_path = ".\\filenameMap.json" # save filename map
filename_map_list = {} # store the map temporarily
folder_map_path = ".\\" + folder_name + "_folderMap.json" # save folder name map
folder_map_list = {}

# get class name
for _, class_dirs, _ in os.walk(work_dir, topdown=False):
	pass
class_num = len(class_dirs)

# change folder name and record
for i in range(class_num):
	class_original = class_dirs[i]
	class_dir_original = os.path.join(work_dir, class_original)
	class_new = "type" + str(i)
	class_dir_new = os.path.join(work_dir, class_new)

	os.rename(class_dir_original, class_dir_new)
	folder_map_list[class_original] = class_new
	folder_map_list[class_new] = class_original

# ensure_ascii is for saving Chinese
jsons = json.dumps(folder_map_list, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
with open(folder_map_path,'w',encoding='utf-8') as f:
	f.write(jsons)

# get new class name
for _, class_dirs, _ in os.walk(work_dir, topdown=False):
	pass


for i in range(class_num):
	class_dir = class_dirs[i]
	class_path = os.path.join(work_dir, class_dir)
	img_list = os.listdir(class_path)
	img_num = len(img_list)

	for j in range(img_num):
		img_original = img_list[j]
		img_dir_original = os.path.join(class_path, img_original)

		if img_original in filename_map_list:
			img_dir_new = os.path.join(class_path, str(filename_map_list[img_original]) + fileType)
		else:
			img_count = img_count + 1
			img_dir_new = os.path.join(class_path, str(img_count) + fileType)
			filename_map_list[img_original] = str(img_count)
			filename_map_list[str(img_count)] = img_original

		os.rename(img_dir_original, img_dir_new)


jsons2 = json.dumps(filename_map_list, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
with open(filename_map_path,'w',encoding='utf-8') as f:
	f.write(jsons2)

print ('Done successfully!')