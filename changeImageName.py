"""

	Step 1: Change the filename to increasing number and save
their map, for opencv do not support file path beyond ASCII.

"""

import os.path
import json

work_dir = ".\\shangHeDouXingTai" # direction of your data
fileType = '.tif' # your data type

# count all unique image, that means if an image was marked as
# more than one class, its name after changed will be the same
img_count = 0

# the map aims to ease the process, is not for training
filename_map_path = ".\\filenameMap.json" # save filename map
filename_map_list = {} # store the map temporarily
folder_map_path = ".\\folderMap.json" # save folder name map
folder_map_list = {}

for _, class_dirs, _ in os.walk(work_dir, topdown=False):
	pass
class_num = len(class_dirs)


for i in range(class_num):
	class_original = class_dirs[i]
	class_dir_original = os.path.join(work_dir, class_original)
	class_new = "type" + str(i)
	class_dir_new = os.path.join(work_dir, class_new)

	os.rename(class_dir_original, class_dir_new)
	folder_map_list[class_original] = class_new
	folder_map_list[class_new] = class_original


jsons = json.dumps(folder_map_list, sort_keys=True, indent=4, separators=(',', ': '))
with open(folder_map_path,'w') as f:
	f.write(jsons)

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
			img_dir_new = os.path.join(class_path, str(filename_map_list[img_original]))
		else:
			img_count = img_count + 1
			img_dir_new = os.path.join(class_path, str(img_count) + fileType)
			filename_map_list[img_original] = str(img_count)
			filename_map_list[str(img_count)] = img_original

		os.rename(img_dir_original, img_dir_new)


jsons2 = json.dumps(filename_map_list, sort_keys=True, indent=4, separators=(',', ': '))
with open(filename_map_path,'w') as f:
	f.write(jsons2)

print ('Done successfully!')