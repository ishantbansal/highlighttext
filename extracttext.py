import cv2
import numpy as np 




def getTextOverlay(input_image) :
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  lower_val = np.array([0,0,0])
  upper_val = np.array([179,90,130])
  mask = cv2.inRange(hsv, lower_val, upper_val)
  output = cv2.bitwise_not(mask)
  return output


if __name__ == '__main__':
  img = cv2.imread("simpsons_frame0.png")
  output = getTextOverlay(img)
  cv2.imwrite('result.png' , output)