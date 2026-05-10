from os import listdir #used to iterate through dataset
import cv2
import cv2.face
import numpy as np

recog=cv2.face.LBPHFaceRecognizer_create()
#recog is object of class LBPH [linear binary pattern histogram] which is useful for face recognition 

root_dir="./dataset"

features=[]#features are images in folder 
labels=[]#name of folder 
i=0

for subfolder in listdir(root_dir):
    
        folder_path=f"{root_dir}/{subfolder}"
        print(f"----------------files of folder {folder_path}-------------------")
        for file in listdir(folder_path):
            file_path=f"{folder_path}/{file}"
            image=cv2.imread(file_path,0)#image holds the features of image and here 0 is used to convert image to gray image
            features.append(image)
            labels.append(i)#after features of all images are stored we need to store the folder as well i,e label (folder name =0)
        

        i=i+1#after coming out of for loop next it needs to store folder 1 so incrementing it 
print(f"Features={features}")
print(f"Labels={labels}")
print(f"Length of features= {len(features)}, Length of labels= {len(labels)}")


#when we are training the machine we need to give input and output .
#all features are the inputs and labels are output, so that system learns 
recog.train(features,np.array(labels))#here labels is having one row with many columns but train() expects array 

# next we need to test whether system got trained or not for that:-
#file_path=f"./dataset/0/myimage12.jpg"
#test_image=cv2.imread(file_path,0)#0 here is used to converting to gray image 
#cv2.imshow("test image ",test_image)#to show the image 
#cv2.waitKey()

# now i will ask lbph to recognise image 
#id,confi=recog.predict(test_image)
#id is the label .if person in folder 1 is correctly identified then id is 0 because our first folder is 0
#conf is the confidence 
#print(f"ID : {id}, Confi : {confi}")

#if conf is 0 it is very good but if it is increasing it means algorithm is not sure about its prediction 
# so far it is working fine with trained dataset 
# check how it behaves for unseen data by taking unknown image 

#file_path="./sachin.jpg"
#test_image=cv2.imread(file_path,0)
#cv2.imshow("test image ",test_image)
#cv2.waitKey()
#id,confi=recog.predict(test_image)
#print(f"ID : {id}, Confi : {confi}")#getting confidence of 90.61088727353759 mapping to folder 0 means some of my facial features are matching myself but confidence is more so not accurate

#till now first we are training and then predicting . so we need to train once and export it 

recog.save("mymodel.yml")#since we are working with image data extension is .yml so we can use this trained model later on 
