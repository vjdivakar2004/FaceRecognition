import cv2

from apidemo import save_to_db#from apidemo.py we are using save_to_db function 

cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam=cv2.VideoCapture(0)

recog=cv2.face.LBPHFaceRecognizer_create()
recog.read('mymodel.yml')

names={0:"vijaya",1:"shalini"}
while True:
    flag,frame=cam.read()

    if flag:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cascade.detectMultiScale(gray,1.1,5)
        if len(faces)>0:

            x,y,w,h=faces[0]
            
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

            roi=gray[y:y+h,x:x+w]  #to extract face from image 
            roi=cv2.resize(roi,(300,300))

            id,confi=recog.predict(roi)
            print(f" Id :{id}, confi: {confi}")

            if confi<30:
                name=names[id]
                save_to_db(name)#whose name gets recognised those names will be saved to database 
            else:
                name="unknown"
            org=(50,50)
            font=cv2.FONT_HERSHEY_SIMPLEX
            font_scale=1.5
            color=(0,0,255)
            thickness=2

            cv2.putText(frame,name,org,font,font_scale,color,thickness)



        cv2.imshow("face recognition ",frame)
        k=cv2.waitKey(5)
        if k==ord('q'):
            break

cam.release()