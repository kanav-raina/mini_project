#face_recognition library to recognize faces
import face_recognition
import subprocess
import time 

known_image = face_recognition.load_image_file("face1.jpg")
test=input("Enter 1 to capture image: " )
if(test==1):
  subprocess.call(['/home/kanav/Desktop/project/file1.sh'])
  time.sleep(3)

unknown_image = face_recognition.load_image_file("face2.jpg")
 
biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
 
results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
if(results[0]):
    print("Unlock the door")
else:
    print("Door is still Lock")
