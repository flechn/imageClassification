"""

	Crop your dataset guided by json generated by labelme.

"""

import os.path
import json
import cv2

folder_name = "shangHeDou_guanZhuangMian_cut" # your data folder's name
work_dir = ".\\" + folder_name # direction of your data
fileType = '.jpg' # your data type

for i in range(200):
	img_path = os.path.join(work_dir, str(i + 1) + fileType)
	json_path = os.path.join(work_dir, str(i + 1) + ".json")

	with open(json_path, 'r') as f:
		jsonTemp = json.load(f)

	left = right = up = down = a = b = x = y = 0
	shapes = jsonTemp["shapes"]
	for shape in shapes:
		if shape["label"] == "shangHeDou":
			a = shape["points"][0][0]
			b = shape["points"][0][1]
			x = shape["points"][1][0]
			y = shape["points"][1][1]
			break

	if a > x:
		a, x = x, a
	if b > y:
		b, y = y, b

	a -= 30
	b -= 30
	x += 30
	y += 50

	left = a if a > 0 else 0
	right = x if x < 823 else 823
	up = b if b > 0 else 0
	down = y if y < 900 else 900

	img = cv2.imread(img_path)
	cropped = img[int(up):int(down), int(left):int(right)]
	cv2.imwrite(img_path, cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

print ('Done successfully!')