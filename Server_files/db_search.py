import sqlite3

'''Module to search database for access rights'''


def lookup_access_rights(recognized_name, db_file="face_data.db"):
        '''Method searches database and returns access rights.

        @params:
            recognized_name: Name to look up
            db_file: Database to search

        @Returns: String
        '''
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()
        query = "SELECT access_rights FROM face_data WHERE name = ?"

        cursor.execute(query, (recognized_name,))
        result = cursor.fetchone()

        connection.close()

        if result:
            access_rights = result[0]
            return access_rights

        else:
            return "Access rights not found for this person"
