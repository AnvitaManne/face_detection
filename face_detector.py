import cv2

from random import randrange
#load some pre-trained data on face frontals from opencv(hear cascade algorithm)
trained_face_data=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

#to capture a video to detect face in
#can put video instead of 0
webcam=cv2.VideoCapture(0)

#iterate forever over frames
while True:
    #read the current _read,frame=webcam.read()

    #must convert frame to grayscale
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

    #draw rectangles around
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),5)
        
    cv2.imshow('Clever Programmer Face Detector',frame)
    #it will wait 1ms and automatically press a key
    key=cv2.waitKey(10)

    #stop if Q key is pressed
    #ascii for q Q
    if key==81 or key==113:
        break

#release the video capture object
webcam.release()



 
'''
import random
#load some pre-trained data on face frontals from opencv(hear cascade algorithm)
trained_face_data=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

#choose an image to detect face in
#import an img
img=cv2.imread("C:\\Users\\91636\\OneDrive\\Desktop\\rdjr.png")

#to convert to black n white
grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

#draw rect around the face
#(top-left point i.e x, y,width,height)
cv2.rectangle(img,(68,24),(68+54,24+54),(0,255,0),2)

for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(random.randrange(256),random.randrange(256),random.randrange(256)),5)

#print(face_coordinates)

#naming the window tht will pop up and displaying img
cv2.imshow('Clever Programmer Face Detector',img)
 
#to keep image open till a key is pressed
cv2.waitKey()
print('code completed')
'''
