import cvzone
import cv2
import numpy as np

# https://www.computervision.zone/lessons/code-and-files-4/

background = cv2.imread("images/erfurt_000003_000019_leftImg8bit.png")
# background = np.ones((480, 640, 3), np.uint8)
foreground = cv2.imread("images/maple-tree.png", cv2.IMREAD_UNCHANGED)
foreground = cv2.resize(foreground, (0, 0), None, 0.25, 0.25)

result = cvzone.overlayPNG(background, foreground, [100, 100])

cv2.imshow("Image", result)
cv2.waitKey(0)