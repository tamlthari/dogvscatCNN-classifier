import psycopg2
import os
import cv2
import base64
import numpy as np

conn = psycopg2.connect(user = 'postgres', database = 'catvdog', password="thuctam")
conn.autocommit = True
cursor = conn.cursor()

def create_table():
    query = f"""CREATE TABLE IF NOT EXISTS catvsdog (
            id SERIAL PRIMARY KEY, 
            img bytea, 
            label int
            );
    """
    # column bytea to accept bytes datatype after encode(), type of column bytea is memoryview
    # Chuyển memoryview về bytes = memoryview.tobytes() . Sau đó decode() là ra array của hình
    cursor.execute(query)

def encode(img_path):
    img = cv2.imread(img_path)
    img = cv2.imencode('.jpg', img)
    img_encoded = base64.b64encode(img[1])
    return img_encoded

def decode(img_encoded):
    img_decoded = base64.b64decode(img_encoded)
    img_decoded = np.frombuffer(img_decoded, dtype=np.uint8)
    img_decoded = cv2.imdecode(img_decoded, 1) # array of image
#     cv2.imwrite('./1.jpg', img_decoded) # if want to restore image
    return img_decoded

def save_into_db(img, label):
    query = f"""
                INSERT INTO catvsdog (img, label) 
                VALUES (%s, %s) 
                RETURNING id;
                """
    img_encoded = encode(img)
    vals = (img_encoded, label)

    cursor.execute(query, vals)
