import numpy as np
import cv2
import datetime
import os

#  Make sure  OpenCV is installed and can be imported by your Python interpretor.

cascPath="D:\\root\\src\\opencv\\sources\\build\\install\\etc\\haarcascades\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(0)
cwd = os.getcwd()
DATE = datetime.datetime.now().date().strftime ("%Y-%m-%d-%H.%M.%S")

def create_path(path):
	print(path)
	if not os.path.exists(path):
	    os.makedirs(path)

folder_path = cwd + "\\" + DATE
create_path(folder_path)

while(True):
	ret, img = cap.read()
	face_frame = None

	faces = faceCascade.detectMultiScale(
		img,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags = cv2.CASCADE_SCALE_IMAGE 
	)

	print "Found {0} faces!".format(len(faces))

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		face_frame =img[y:y+h,x:x+w]

	if(len(faces)>0):
		filename = datetime.datetime.now() .strftime ("%Y-%m-%d-%H.%M.%S")
		image_file_name = str(filename) + str(".png")
		complete_path = folder_path + "\\" + image_file_name
		print(complete_path)
		#cv2.imwrite(complete_path,img)
		cv2.imwrite(complete_path,face_frame)

	cv2.namedWindow("Camera #3",cv2.WINDOW_NORMAL)
	cv2.imshow("Camera #3", img) 

	key = cv2.waitKey(10)
	# Key 32 is SpaceBar.
	if key == 27 or key == 32:
		break

    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()