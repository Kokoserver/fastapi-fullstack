from pymongo import MongoClient
from decouple import config


import smtplib
from decouple import config
from starlette.background import BackgroundTasks

def mail():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("owonikokoolaoluwa@gmail.com", "ksbdcllupwjkgufk")
        subject = "owonikoko ennebee"
        body = "testing email aadress"
        msg = f"subject: {subject}\n\n{body}"
        BackgroundTasks(tasks=[ smtp.sendmail( "owonikokoolaoluwa@gmail.com", "owonikokoolaoluwa@gmail.com", msg)])
        print("done sending")


