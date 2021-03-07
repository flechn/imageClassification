"""

	Step 3: If your dataset is made from the same environment
(e.g., from screenshot of the whole screen), that means your 
image data share the same size, and share the same noise which
may interfere training process.
	
	Aim to crop your images automatically, we should obtain
the location of region we need, that is Step 3's task.

	If your image is too large, unfortunately this tool is not
a wise choice for you.

from https://blog.csdn.net/qq_41360787/article/details/103258773

"""

import cv2
import numpy as np

img = cv2.imread('sample.jpg')

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDOWN:
		xy = "%d, %d" % (x, y)
		cv2.circle(img, (x, y), 1, (255, 0, 0), thickness = -1)
		cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
					1.0, (0,0,0), thickness = 1)
		cv2.imshow("image", img)

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
while(1):
	cv2.imshow("image", img)
	if cv2.waitKey(0) & 0xFF == 27:
		break

cv2.destroyAllWindows()