import cv2
cam=cv2.VideoCapture(0)#0 indicates default cam and cam is object here 

while True:
    flag,frame=cam.read()#to capture the image flag holds the boolean value and frame holds captured image in the form of  matrix 

    if flag:
        print(f"image got captured ")

        cv2.imshow("my image ",frame)
      
       # cv2.imwrite("myimage.jpg",frame)#to save the captured image 
        k=cv2.waitKey(10)

        if k==ord('q'):
            break


    else:
        print("something went wrong")

