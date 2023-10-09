#!/usr/bin/python3

import os
import face_recognition
import pickle

'''Module trains the face recognition model on provided data set'''


dataset_dir = "images"

known_face_encodings = []
known_face_names = []


for person_dir in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person_dir)

    for image_file in os.listdir(person_path):
        image_path = os.path.join(person_path, image_file)

        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)

        if len(face_encoding) > 0:
            known_face_encodings.append(face_encoding[0])
            known_face_names.append(person_dir)

with open("known_faces.pkl", "wb") as f:
    pickle.dump((known_face_encodings, known_face_names), f)

print("Training completed. Model saved as 'known_faces.pkl'.")
