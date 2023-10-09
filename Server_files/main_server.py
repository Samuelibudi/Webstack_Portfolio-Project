#!/usr/bin/python3

import socket
import pickle
import face_recognition
import recognition
import base64
import numpy as np
import cv2
from db_search import lookup_access_rights

'''Module configures a server to listen to port 50000
   receives an image and sends it for facial recognition.
   It then returns the access rights to the client.'''


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(1)
print("Server listening on port 8080")

while True:
    client_socket, addr = server_socket.accept()
    client_soket.settimeout(30)
    print(f"Accepted connection from {addr}")

    chunk_size = 4096

    try:
        image_data_base64 = b""
        while True:
            try:
                chunk = client_socket.recv(chunk_size)
                if not chunk:
                    break
                image_data_base64 += chunk
            except socket.timeout:
                print("Socket timeout (no data received)")
                break
            except Exception as e:
                print(f"Error while receiving data: {str(e)}")
                break

        if len(image_data_base64) % 4 != 0:
            padding_needed = 4 - (len(image_data_base64) % 4)
            padding = b'=' * padding_needed
            image_data_base64 += padding

        recognized_names = recognition.recognize_face(image_data_base64)

        if recognized_names:

            access_rights = lookup_access_rights(recognized_name)

            client_socket.send(pickle.dumps(access_rights))

        else:
            client_socket.send(b"Access Denied!")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
