import picamera


def preview_mode(cam, h_res, v_res, x_0, y_0):
    cam.start_preview(fullscreen=False, window=(x_0, y_0, h_res, v_res))
    while True:
        t_clavier = input("Presser la touche <s> puis <ENTER> pour sotir de ce mode : \n")
        if t_clavier == "s":
            cam.stop_preview()
            break


if __name__ == '__main__':

    camera = picamera.PiCamera()
    preview_mode(camera, 640, 480, 1000, 0)
