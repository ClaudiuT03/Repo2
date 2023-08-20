"""Scriptul main unde avem API endpoint-urile"""
import json

# dupa ce am instalat libraria cu: pip install flask
from flask import Flask, request, Response

import crud_sqlite as crud


from database_sqlite import open_db

app = Flask(__name__)
db_connection = open_db()  # ne cream o conexiune globala la DB pe care sa o refolosim in toate API-urile 


# API endpoints

# get all users
@app.route("/users", methods=["GET"])
def read_all_users():
    # TODO: trebuie afisat user-ul mai citet, cu parola ascunsa si id scos din raspuns!!
    status_code, response_body = crud.get_users(db_connection)  # apelam functia crud care se ocupa de extragerea datelor necesare din db
    return Response(status=status_code, response=json.dumps(response_body))  # returnam response-ul catre client


@app.route("/users/add_user", methods=["POST"])
def create_user():
    user_data = json.loads(request.data)  # luam datele de adaugam de pe body-ul requestului
    status_code, response_body = crud.add_user(db_connection, user_data)
    return Response(status=status_code, response=json.dumps(response_body))


if __name__ == '__main__':  # prima linie de cod care se citeste (dupa import-uri) in momentul in care rulam fisierul ca un script: python main.py
    app.run(debug=True, port=7000)