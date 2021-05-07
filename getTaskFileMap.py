"""

	This tool is used to generate maps which record every task's
file number, which can remove data redundancy, then we can just
keep one copy of the dataset.

	The generated json file will save every file name seperated
by type. For example, if a task has 3 tasks, the json will be
like {"type0":{1, 3}, "type1":{2}, "type2":{4, 5}}

"""

import os.path
import json

folder_name = "shangHeDouXingTai_1_jpg" # your data folder's name
work_dir = ".\\" + folder_name # direction of your data

# the map aims to ease the process, is not for training, at least not now
map_path = ".\\" + folder_name + "_taskFileMap.json" # save folder name map
map_list = {}

# get class name 
for _, class_dirs, _ in os.walk(work_dir, topdown=False):
	pass
class_num = len(class_dirs)


for i in range(class_num):
	class_dir = class_dirs[i]
	class_path = os.path.join(work_dir, class_dir)
	img_list = os.listdir(class_path)
	img_num = len(img_list)

	list_temp = []

	for j in range(img_num):
		list_temp.append(img_list[j][:-4])

	map_list[class_dir] = list_temp

jsons = json.dumps(map_list, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
with open(map_path,'w',encoding='utf-8') as f:
	f.write(jsons)

print ('Done successfully!')