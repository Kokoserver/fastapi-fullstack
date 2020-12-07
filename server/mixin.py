from fastapi import status
from server.setting import email, password
from fastapi.responses import JSONResponse
from fastapi.background import BackgroundTasks
from .db import Database
import bcrypt
import smtplib

def getData(observable:dict, mode:bool = True):
        if mode:
            return [data for data in observable]
        else:
             for data in observable:
                return data
            


def hashpassword(password):
    return bcrypt.hashpw(password , bcrypt.gensalt())


def checkpassword(password:bytes, hashpassword:bytes):
    return bcrypt.checkpw(password ,hashpassword)

def mail(message:str, subject:str):
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(email, password)
    subject = subject
    body = message
    msg = f"subject: {subject}\n\n{body}"
    server.sendmail(email, "owonikokoolaoluwa@gmail.com", msg)




def databaseconnect():
    try:
        Database.connectDb()
    except:
        return str("Error establisging database connection")
       

def  Response(data, code):
    return JSONResponse(data, status_code=code)


