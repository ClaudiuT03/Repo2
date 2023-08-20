"""Functiile CRUD asupra DB-ului"""
import uuid

from models_sqlite import User, Book

def get_users(db_connection):
    # functia CRUD de returnare a tuturor userilor din DB.
    # rulam un sql query si returnam un status_code si un mesaj/date
    # daca avem exceptie pe DB, returnam 500 si mesajul exceptiei, 
    # daca nu avem useri in db returnam 404 si mesajul "No users...",
    # iar daca totul functioneaza corect, returnam 200 si lista de useri
    SQL_QUERY = "SELECT * FROM Users;"
    try:
        cursor = db_connection.cursor()
        cursor.execute(SQL_QUERY)  # executam sql query-ul
    except Exception as e:
        return 500, f"Server error: {e}"
    else:
        users = cursor.fetchall()
        if users:
            return 200, users
        else:
            return 404, f"No users in DB!"


def add_user(db_connection, user_data):
    user_data['id'] = str(uuid.uuid4())   # datele introduse de client
    user_obj = User(**user_data)          # cream obiectul User (care seteaza si is_logged)
    if not user_obj.validate():
        return 400, f"User validation error!"

    SQL_QUERY = "INSERT INTO Users(id, name, password, email, is_logged) VALUES (:id, :name, :password, :email, :is_logged);"
    try:
        cursor = db_connection.cursor()
        cursor.execute(SQL_QUERY, user_obj.__dict__)  # inlocuim VALUES din SQL_QUERY cu valorile adevarate din dict-ul aferent obiectului user_obj 
        db_connection.commit()
    except Exception as e:
        return 500, f"Server error: {e}"
    else:
        return 201, f"User with id={user_data['id']} has been successfully created!"