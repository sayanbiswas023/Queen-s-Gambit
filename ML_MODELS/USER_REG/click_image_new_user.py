# import cv2
# import imutils
# import time
# import os
# import face_recognition

# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# present_path=os.getcwd()

# def takePicture(username:str):

#     cam = cv2.VideoCapture(0)
  
#     # reading the input using the camera
#     result=False

#     while result == False:
#         print("Please retake image")
#         result, image = cam.read()
#         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#         face_locations = face_recognition.face_locations(image)
#         while len(face_locations) <0:
#             print("No face detected")
#             result, image = cam.read()
#             image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#             face_locations = face_recognition.face_locations(image)
#         encode = face_recognition.face_encodings(image)[0]
#     cam.release()
    
#     image_path= os.path.join(present_path,'USER_IMAGES',str(username)+'.jpg') 
#     cv2.imwrite(image_path, image)
#     print(image_path)
#     return image_path

# print(takePicture('PataNhiKaun'))
# img=cv2.imread(takePicture('PataNhiKaun'))
# cv2.imshow(img)
# cv2.waitkey(0)






import cv2
import os
import face_recognition

def capture_image(username:str):
    present_path=os.getcwd()
    print(present_path)
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0

    while True:
        ret, frame = cam.read()
        face_locations = face_recognition.face_locations(frame)
#         while len(face_locations) <0:
        if not ret or len(face_locations)<0:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k%256 == 32:
            # SPACE pressed
            img_name = os.path.join(present_path,"ML_MODELS","USER_REG","USER_IMAGES","User_{}.png".format(username))
            cv2.imwrite(img_name, frame)
            print("{} registered!".format(username))
            img_counter += 1
            break

    cam.release()

    cv2.destroyAllWindows()

capture_image('PataNhiKaun')