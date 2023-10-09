import cv2
from picamera import PiCamera
import numpy as np
import requests
import io

'''Module establishes connection with remote server
   captures and sends image'''


server_url = 'https://127.0.0.1:8080/'

def establish_connection():
    '''Method establishes connection with remote server

    @params: Non
    @Returns: boolean
    '''

    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Connection error: {str(e)}")
        return False

def capture_image_on_face_detection():
    '''Captures images continously until a face is detected
    It also establishes connection with backend server and 
    sends captured image and waits for a response

    '''


    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')                                             
    camera = PiCamera()
    camera.resolution = (640, 480)

    while True:
        image_path = 'captured_face.jpg'
        camera.capture(image_path)
        frame = cv2.imread(image_path)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) > 0:
            (x, y, w, h) = faces[0]
            extracted_face = frame[y:y+h, x:x+w]

        if not establish_connection():
            return 3

        try:
            image_bytes = cv2.imencode('.jpg', extracted_face)[1].tobytes()

            files = {'image': ('face_image.jpg', image_bytes)}

            response = requests.post(server_url, files=files)

            if response.status_code == 200:
                access_rights = response.json().get('access_rights')
                return access_rights
            else:
                return 2

        except Exception as e:
            return 3
