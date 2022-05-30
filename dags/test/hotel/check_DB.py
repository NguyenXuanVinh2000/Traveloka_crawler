from tabnanny import check
import mysql.connector
import smtplib
import os
import os

MYSQL_HOST = "10.10.5.68"
MYSQL_DB = "HOTEL"
MYSQL_TABLE = "hotel"
MYSQL_USER ="root"
MYSQL_PASSWORD = "airflow"
MYSQL_PORT = 3306
MYSQL_UPSERT = False
MYSQL_RETRIES = 3
MYSQL_CLOSE_ON_ERROR = True
MYSQL_CHARSET = 'utf-8'

mydb = mysql.connector.connect(
  host=MYSQL_HOST,
  user=MYSQL_USER,
  password=MYSQL_PASSWORD,
  database=MYSQL_DB
)

def check_data(hotel_name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT hotel_name FROM hotel")
    myresult = mycursor.fetchall()
    for x in myresult:
        old_hotel = x
        old_hotel = str(old_hotel)
        old_hotel = old_hotel.replace('(','')
        old_hotel = old_hotel.replace(')','')
        old_hotel = old_hotel.replace(',','')
        old_hotel = old_hotel.replace("'",'')
        if str(hotel_name)== old_hotel:
            return True
    return False

