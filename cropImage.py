"""

	Step 4: Crop your dataset in-place.

"""

import os.path
import cv2

work_dir = ".\\shangHeDouXingTai" # direction of your data

for _, class_dirs, _ in os.walk(work_dir, topdown=False):
	pass
class_num = len(class_dirs)

for i in range(class_num):
	class_dir = class_dirs[i]
	class_dir_original = os.path.join(work_dir, class_dir)
	img_list = os.listdir(class_dir_original)
	img_num = len(img_list)

	for j in range(img_num):
		img_name = img_list[j]
		img_dir = os.path.join(class_dir_original, img_name)
		img = cv2.imread(img_dir)
		cropped = img[100:1356, 315:2560]
		cv2.imwrite(img_dir, cropped)


print ('Done successfully!')