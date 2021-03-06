"""

	step 2: change the format to (.jpg)

"""

import os.path
import cv2
import json

work_dir = ".\\shangHeDouXingTai_O" # direction of your data
output_dir = ".\\shangHeDouXingTai" # direction of output
if(not os.path.exists(output_dir)):
	os.mkdir(output_dir)

for _, class_dirs, _ in os.walk(work_dir, topdown=False):
	pass
class_num = len(class_dirs)

for i in range(class_num):
	class_dir = class_dirs[i]
	class_dir_original = os.path.join(work_dir, class_dir)
	class_dir_new = os.path.join(output_dir, class_dir)
	if(not os.path.exists(class_dir_new)):
		os.mkdir(class_dir_new)

	img_list = os.listdir(class_dir_original)
	img_num = len(img_list)
	for j in range(img_num):
		img_name = img_list[j]
		img_dir = os.path.join(class_dir_original, img_name)
		img = cv2.imread(img_dir, 1)

		if filenameChange:
			if img_name in filename_map_list:
				img_dir_new = os.path.join(class_dir_new, filename_map_list[img_name] + '.jpg')
			else:
				img_count = img_count + 1
				img_dir_new = os.path.join(class_dir_new, str(img_count) + '.jpg')
				filename_map_list[img_name] = img_count
				filename_map_list[img_count] = img_name
		else:
			img_dir_new = os.path.join(class_dir_new, img_name[:-4] + '.jpg')
		# print(img.shape)

		img.save(img_dir_new)


print ('Done successfully!')