# >--------------------------------------- DATABASE ------------------------------------------------------------------<

import base64
import random
import sqlite3

from data.logger import SENT_TO_LOG
from data.constants import *
# directorio de la base de datos
DB_FILE = os.path.join(APP_DATA, "user_data.db")

def CREATE_DB():
    # si no existe la creo
    if not os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "w") as db:
                db.write("")
        except Exception as e:
            msg = f"No se pudo crear el archivo DB > {e.args}"
            print(msg)
            SENT_TO_LOG(msg)
        else:
            # creo las tablas con sus columnas
            with sqlite3.connect(DB_FILE) as temp_conexion:
                temp_cursor = temp_conexion.cursor()
                #query_delete = """DROP TABLE "main"."users";"""
                query_users = """CREATE TABLE IF NOT EXISTS "main"."users" (
                "user" text NOT NULL,
                "password" text,
                "first_connection" TEXT,
                "last_time_connected" TEXT,
                "connected_time" TEXT,
                "left_time" TEXT,
                PRIMARY KEY ("user") ON CONFLICT IGNORE
                );"""
                temp_cursor.execute(query_users)
                #
                query_pamarillas = """CREATE TABLE IF NOT EXISTS "main"."pamarillas_searches" (
                "site" text NOT NULL PRIMARY KEY,
                "place" text
                );"""
                temp_cursor.execute(query_pamarillas) #"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

def encode_passw(texto):
    try:
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        abc_lower = abc.lower()
        # CAESAR
        # cantidad de desplazamiento
        n = random.randint(2, 8)
        # Variable para guardar mensaje cifrado
        cifrado = ""
        # Iteramos por cara letra del mensaje
        for l in texto:
            # Si la letra está en el abecedario se reemplaza
            if l in abc:
                pos_letra = abc.index(l)
                # Sumamos para movernos a la derecha del abc
                nueva_pos = (pos_letra + n) % len(abc)
                cifrado += abc[nueva_pos]
            elif l in abc_lower:
                pos_letra = abc_lower.index(l)
                # Sumamos para movernos a la derecha del abc
                nueva_pos = (pos_letra + n) % len(abc)
                cifrado += abc_lower[nueva_pos]
            else:
                # Si no está en el abecedario sólo añadelo
                cifrado += l
        caesar = f"{n}{cifrado}"
        base64_caesar_encoder = base64.encodebytes(caesar.encode("utf-8"))
        return base64_caesar_encoder.decode("utf-8")
    except Exception as e:
        SENT_TO_LOG(f"Codificando contraseña {e.args}", "ERROR")

def decode_passw(texto):
    try:
        if type(texto) == str:
            texto = texto.encode("utf-8")
        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        abc_lower = abc.lower()
        #
        base64_caesar_encoded_passw = base64.decodebytes(texto)
        texto = base64_caesar_encoded_passw.decode("utf-8")
        i = int(texto[0])
        # Guardar posible mensaje
        descifrado = ""
        for l in texto:
            # Si la letra está en el abecedario reemplazamos
            if l in abc:
                pos_letra = abc.index(l)
                # Restamos para movernos a la izquierda
                nueva_pos = (pos_letra - i) % len(abc)
                descifrado += abc[nueva_pos]
            elif l in abc_lower:
                pos_letra = abc_lower.index(l)
                # Restamos para movernos a la izquierda
                nueva_pos = (pos_letra - i) % len(abc)
                descifrado += abc_lower[nueva_pos]
            else:
                descifrado += l
        return descifrado[1:]
    except Exception as e:
        SENT_TO_LOG(f"Decodificando contraseña {e.args}", "ERROR")

def SELECT_USERS():
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con.cursor()
            query = """SELECT * FROM "main"."users"; """
            cur.execute(query)
            selection = cur.fetchall()
            if selection is not None:
                return selection
            return ()
    except Exception as e:
        SENT_TO_LOG("Seleccionando usuarios de la DB", "ERROR")

def GET_USERSNAMES():
    try:
        return [i[0] for i in SELECT_USERS()]
    except Exception as e:
        SENT_TO_LOG("Seleccionando usuarios de la DB", "ERROR")

def SELECT_ONE_USER(phone):
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con.cursor()
            query = """SELECT * FROM "main"."users" WHERE "users"."user" = ?; """
            cur.execute(query, [phone])
            selection = cur.fetchone()
            return selection
    except Exception as e:
        SENT_TO_LOG("Seleccionando un usuario de la DB", "ERROR")

# agregar usuario
def ADD_USER(user, passw):
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con. cursor()
            query = """INSERT INTO "main"."users" ("user", "password") VALUES (?, ?);"""
            cur.execute(query, [user, encode_passw(passw) if passw != "" else ""])
            con.commit()
    except sqlite3.Error as e:
        SENT_TO_LOG(f"Añadiendo usuario a la DB {e.args}", "ERROR")

# actualizar contrasenna
def UPDATE_PASSW(user, passw):
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con.cursor()
            query = """UPDATE "main"."users" SET "password" = ? WHERE user= ?"""
            cur.execute(query, [passw, user])
            con.commit()
    except sqlite3.Error as e:
        SENT_TO_LOG(f"Actualizando usuario en la DB {e.args}", "ERROR")
        raise e

# actualizar tiempo
def UPDATE_TIME(user, current, left, first, last):
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con.cursor()
            query = """UPDATE "main"."users" SET "first_connection" = ? WHERE user= ? AND "first_connection" = '' OR "first_connection" ISNULL"""
            cur.execute(query, (first,user))
            query = """UPDATE "main"."users" SET "last_time_connected" = ?, "connected_time" = ?, "left_time" = ? WHERE user= ?"""
            cur.execute(query, [last, current, left, user])
            con.commit()
    except sqlite3.Error as e:
        SENT_TO_LOG(f"Actualizando datos del Usuario en la DB {e.args}", "ERROR")
        raise e

# eliminar usuario
def DEL_USER(user):
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con.cursor()
            query = """DELETE FROM "main"."users" WHERE "user" = ?;"""
            cur.execute(query, [user,])
            con.commit()
    except sqlite3.Error as e:
        SENT_TO_LOG(f"Eliminando usuario de la DB {e.args}", "ERROR")
        raise e
    
# agregar usuario
def ADD_PAMARILLAS_SEARCH(site, place):
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con. cursor()
            query = """INSERT INTO "main"."pamarillas_searches" ("site", "place") VALUES (?, ?);"""
            cur.execute(query, [site, place])
            con.commit()
    except sqlite3.Error as e:
        SENT_TO_LOG(f"Añadiendo busqueda en PAMARILLAS a la DB {e.args}", "ERROR")
        
def SELECT_PAMARILLAS_SEARCH():
    try:
        with sqlite3.connect(DB_FILE) as con:
            cur = con.cursor()
            query = """SELECT * FROM "main"."pamarillas_searches"; """
            cur.execute(query)
            selection = cur.fetchall()
            if selection is not None:
                return selection
            return ()
    except Exception as e:
        SENT_TO_LOG("Seleccionando usuarios de la DB", "ERROR")
        
def GET_PAMARILLAS_SEARCH_CATEG():
    try:
        return [i[0] for i in SELECT_PAMARILLAS_SEARCH()]
    except Exception as e:
        SENT_TO_LOG("Seleccionando categorias de PAmarillas de la DB", "ERROR")
        
def GET_PAMARILLAS_SEARCH_PLACE():
    try:
        return [i[1] for i in SELECT_PAMARILLAS_SEARCH()]
    except Exception as e:
        SENT_TO_LOG("Seleccionando lugares de PAmarillas de la DB", "ERROR")