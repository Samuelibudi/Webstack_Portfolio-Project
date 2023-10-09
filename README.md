## Webstack_Portfolio-Project

The project is a design of a facial recognition system used to unlock doors.
The project uses a Raspberry pi 3 which communicates with a backend server to get the access rights of an individual.

## Technologies used
- Raspberry pi 3
- Python3
- Opencv library
- Face recognition and Dlib libraries

| **Tasks** | **Description** |
|-----------|-----------------|
| Raspberry_pi_files/main.py | Main script running on the raspberry pi |
| Raspberry_pi_files/detect_face.py | Runs on raspberry pi. Continoulsy takes pictures until it detects a face |
| Server_files/db_search | Searches database for access_rights corresponding to a name |
| Server_files/folder_labels.py | Creates folder with images to facilitate training |
| Server_files/main_server.py | Server script that listens on socket 8080 for incoming traffic and manages it |
| Server_files/manage_database.py | Creates and manages database |
| Server_files/recognition.py | Handles facial recognition and returns name of recognised face |
| Server_files/trainer | Trains the model on the pictures stored in the images folder |

## Usage

The files in the Raspberry_pi_files folder are meant to run on a raspberry pi

The files in Server_files are meant to run on the backend server
