import picamera


def preview_record_mode(cam, nom_fichier,  h_res, v_res, x_0, y_0):
    cam.start_preview(fullscreen=False, window=(x_0, y_0, h_res, v_res))
    cam.start_recording(nom_fichier)
    while True:
        t_clavier = input("Presser la touche <s> puis <ENTER> pour sotir de ce mode : \n")
        if t_clavier == "s":
            cam.stop_preview()
            cam.stop_recording()
            break


if __name__ == '__main__':

    camera = picamera.PiCamera()
    preview_record_mode(camera, "test.h264",  640, 480, 1000, 0)
