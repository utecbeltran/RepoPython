import Adafruit_DHT
import smtplib
import imaplib
import email
import os
import datetime
import RPi.GPIO as GPIO
import time
host_send="smtp.gmail.com"
host_resive="imap.gmail.com"
username="raspberrypi3utec@gmail.com"
password="1guanodonte"
port=25
port_res=993
mensage_de_error="Lo siento no lo he entendido"

def musica(cancion):
    os.system("mpg321"+" "+cancion)
def actuar():
    numero_correos_actual=["hola"]
    cuerrent_correos=["mundo"]

    email_ree=imaplib.IMAP4_SSL(host_resive,port_res)
    email_ree.login(username,password)
    email_ree.select("inbox")
    status, count = email_ree.select('Inbox')
    for x in count[0]:
        numero_correos_actual[0]=x
    while 1 == True :
        email_ree=imaplib.IMAP4_SSL(host_resive,port_res)
        email_ree.login(username,password)
        email_ree.select("inbox")
        status, count = email_ree.select('Inbox')
        for x in count[0]:
            cuerrent_correos[0]=x
        if numero_correos_actual[0] != cuerrent_correos[0]:
            return True
        numero_correos_actual[0] = cuerrent_correos[0]

def replay(host, port , username , password, mail_to_send, mensage):
    email_conn=smtplib.SMTP(host,port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username,password)
    email_conn.sendmail(username,mail_to_send,mensage)
    email_conn.quit()

def read(host , port , username , password ):
    email_ree=imaplib.IMAP4_SSL(host_resive,port_res)
    email_ree.login(username,password)
    email_ree.select("inbox")
    status, count = email_ree.select('Inbox')
    type, dat=email_ree.search(None, "ALL")
    mail_ids = dat[0]
    id_list = mail_ids.split()
    primero = id_list[0]
    ultimo = id_list[-1]
    status, data = email_ree.fetch(ultimo,'(RFC822)')
    email_body = data[0][1]
    msg= email.message_from_bytes(email_body)
    global body
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True) #to control automatic email-style MIME decoding (e.g., Base64, uuencode, quoted-printable)
                body = body.decode()
                print(body)

            elif part.get_content_type() == "text/html":
                continue
    body=body.split()
def replay(host, port , username , password, msg):
    email_conn=smtplib.SMTP(host_send,port)
    email_conn.starttls()
    print(email_conn.login(username,password))
    email_conn.sendmail(username,"luis.miranda@utec.edu.pe",msg)
    email_conn.quit()




while actuar()==True:
    read(host_resive, port_res, username, password)
    cuerpo=body

    for palabras1 in cuerpo:

        if palabras1== "pon":
            for palabras2 in cuerpo:

                if palabras2 == "cancion":
                    id=cuerpo.index("cancion")
                    cancion= cuerpo[id+1]
                    musica(cancion)
                    break
        elif palabras1=="apaga"and "luz":
            
                
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(18,GPIO.OUT)
                GPIO.output(18,GPIO.LOW)
                print("apagado")
                break
            
        elif palabras1=="prende" and "luz":
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(18,GPIO.OUT)
                GPIO.output(18,GPIO.HIGH)
                print("apagado")
                print("prendido")
                break
