import glob
import tkinter as tk
from PIL import ImageTk, Image


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.lire_images()
        self.creer_widgets()
        self.pack()

    def lire_images(self):
        path_images = glob.glob('./images/*.png')
        self.images = [Image.open(img) for img in path_images]
        self.image_idx = 0

    def mise_a_jour_image(self):
        img = ImageTk.PhotoImage(self.images[self.image_idx])
        self.label.configure(image=img)
        self.label.image = img

    def image_precedente(self):
        self.image_idx = (self.image_idx - 1) % len(self.images)
        self.mise_a_jour_image()

    def image_suivante(self):
        self.image_idx = (self.image_idx + 1) % len(self.images)
        self.mise_a_jour_image()

    def creer_widgets(self):
        img = ImageTk.PhotoImage(self.images[self.image_idx])
        self.label = tk.Label(self, image=img)
        self.label.image = img
        self.suivant = tk.Button(self, text='Suivant',
                                 command=self.image_suivante)
        self.precedent = tk.Button(self, text='Precedent',
                                   command=self.image_precedente)

        self.label.pack()
        self.precedent.pack()
        self.suivant.pack()


fenetre = tk.Tk()
app = Application(master=fenetre)
app.mainloop()
