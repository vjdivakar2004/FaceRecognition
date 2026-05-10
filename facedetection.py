#this file is used to crop the face and store it in respective folders of dataset 

import cv2
import random
cam=cv2.VideoCapture(0)

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#cascade is the object to  refer to .xml file
while True:

    flag,test_image=cam.read()

    if flag:
        test_image_gray=cv2.cvtColor(test_image,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("Face detection",test_image)
        #cv2.waitKey()
        faces=cascade.detectMultiScale(test_image_gray,1.1,5)
        if len(faces)>0:

            x,y,w,h=faces[0]
            print(f"x={x},y={y},w={w},h={h}")
            cv2.rectangle(test_image,(x,y),(x+w,y+h),(0,0,255),2)

            #print(faces)
            cv2.imshow("Face detection",test_image)
            k=cv2.waitKey(5)
            if k==ord('q'):
                break
            if k==ord('s'):
                n=random.randint(1,100)
                roi=test_image[y:y+h,x:x+w]#roi is region of interest i.e face alone   so slicing is done here 
                roi=cv2.resize(roi,(300,300))
                fpath=f"./dataset/0/myimage{n}.jpg"#store the image in given file path 
                cv2.imwrite(fpath,roi)
                
            


cam.release()
