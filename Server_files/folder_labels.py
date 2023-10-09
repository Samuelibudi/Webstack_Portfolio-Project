import cv2
import os

'''Module captures images to be used for training model'''


def image_capture ():

    camera = cv2.VideoCapture(0)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    if not os.path.exists('images'):
        os.mkdir('images')

    name = input("Enter the person's name: ")

    person_folder = os.path.join('images', name)
    if not os.path.exists(person_folder):
        os.mkdir(person_folder)

    image_counter = 1

    while True:

        ret, frame = camera.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            if image_counter > 40:
                print("Maximum of 40 images captured.")
                break

            face_image = frame[y:y+h, x:x+w]

            image_path = os.path.join(person_folder, f'{name}_{image_counter}.jpg')
            cv2.imwrite(image_path, face_image)

            print(f"Face saved as {image_path}")

            image_counter += 1

            if image_counter > 40:
                break
    camera.release()

if __name__ == "__main__"
