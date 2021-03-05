"""

	first step: change the format to (.jpg)

	additionally, change the filename to increasing number and
save their map

"""

import os.path
import cv2

filenameChange = True # if False, filename remains unchanged
filename_map_path = "./filenameMap.json" # save filename map
filename_map_list = []

folder_map_path = "./folderMap.json" # save folder name map
work_dir = "./"                      # direction of your data
class_dirs = os.listdir(work_dir)


for class_dir in class_dirs:



folder_input = './test'
folder_output = './a'  # save output to a different folder

img_list1 = os.listdir(img_fold_A)
num_imgs1 = len(img_list1)
for i in range(num_imgs1):
    name_A = img_list1[i]
    path_A = os.path.join(img_fold_A, name_A)
    im_A = cv2.imread(path_A, 1)
    file_name_temp = name_A[:-4]
    file_name = os.path.join(save_fold_A , file_name_temp+'.jpg')
    cv2.imwrite(file_name, im_A)