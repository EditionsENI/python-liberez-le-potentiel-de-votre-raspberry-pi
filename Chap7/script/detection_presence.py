import picamera
from PIL import Image
import numpy as np
import time
import io
import smtplib


def save_seq_img(cam, nom_fichier):
    cpt = 0

    while cpt < 10:
        filename = nom_fichier + str(cpt) + ".jpeg"
        cam.capture(filename)
        time.sleep(30)
        cpt += 1


def envoi_email():
    fromaddr = 'adresse_expe@gmail.com'
    toaddrs = 'adresse_dest@gmail.com'
    msg = 'Detection presence !'
    username = 'mon_compte@gmail.com'
    password = 'mot_passe'

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


def process(cam, nom_fichier,  h_res, v_res, x_0, y_0):
    cam.start_preview(fullscreen=False, window=(x_0, y_0, h_res, v_res))
    cam.capture("img_init.jpeg")
    img = Image.open("img_init.jpeg").convert("LA")
    img_np = np.array(img)
    stream = io.BytesIO()
    while True:
        cam.capture(stream, format="jpeg")
        stream.seek(0)
        img_rt = Image.open(stream).convert("LA")
        img_rt_np = np.array(img_rt)
        img_sub = np.abs(img_np[0] - img_rt_np[0])

        nb_pixel_sup = np.count_nonzero(img_sub > 25)
        if(nb_pixel_sup > (img_sub.shape[0]*img_sub.shape[1]) * 0.3):
            # envoi d'un email
            # envoi_email()
            # sauvegarde d'images toutes les 30sec pendans 5 min
            save_seq_img(cam, nom_fichier)


if __name__ == '__main__':

    camera = picamera.PiCamera()
    process(camera, "save", 640, 480, 1000, 0)
