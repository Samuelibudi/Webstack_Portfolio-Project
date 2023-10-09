#!/usr/bin/python3

import face_recognition
import pickle
import logging
import numpy as np
import base64
import cv2
from io import BytesIO

'''This module receives images and performs face recognition'''


def recognize_face(image_base64, known_faces_path="known_faces.pkl", tolerance=0.75):
    '''Method takes in an image path and performs recognition

    @params
        image_path: Path to the image

        known_faces_path: Path to trained model

        tolerance: Model threshold
    '''
    try:

        with open(known_faces_path, "rb") as f:
            known_face_encodings, known_face_names = pickle.load(f)

        if len(image_base64) % 4 != 0:
            padding_needed = 4 - (len(image_base64) % 4)
            padding = b'=' * padding_needed
            image_base64 += padding

        binary_data = base64.b64decode(image_base64)

        image_stream = BytesIO(binary_data)

        image_np = cv2.imdecode(np.frombuffer(image_stream.read(), np.uint8), cv2.IMREAD_COLOR)
        
        face_locations = [(0, image_np.shape[1], image_np.shape[0], 0)]

        face_encodings = face_recognition.face_encodings(image_np, face_locations)

        best_match_name = "Unknown"
        best_match_distance = 1.0

        for face_encoding in face_encodings:
            name = "Unknown"

            for i, known_face_encoding in enumerate(known_face_encodings):
                match = face_recognition.compare_faces([known_face_encoding], face_encoding, tolerance=tolerance)

                if match[0]:
                    name = known_face_names[i]
                    break

            face_distances = face_recognition.face_distance([known_face_encoding], face_encoding)
            if face_distance[0] < best_match_distance:
                best_match_name = name
                best_match_distance = face_distances[0]

        return best_match_name
    except Exception as e:
        logging.error(f"An error occured in recognize_face: {e}")
        return "Error"
