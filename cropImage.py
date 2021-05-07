"""

	Step 4: Crop your dataset in-place.

"""

import os.path
import cv2

work_dir = ".\\shangHeDouNeiBiQianHouJuLi_14_jpg" # direction of your data

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
		#cropped = img[100:1356, 915:2560] # guanZhuangMian 1-11
		cropped = img[100:1335, 650:2250] # shiZhuangMian 12-14
		#cropped = img[0:1256, 0:823] # shang_he_dou need the left part
		cv2.imwrite(img_dir, cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


print ('Done successfully!')