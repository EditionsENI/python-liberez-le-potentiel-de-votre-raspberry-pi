import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.creer_ligne_sasie()
        self.creer_bouton()
        self.pack()

    def imprimer_saisie(self):
        print(self.texte.get())

    def creer_bouton(self):
        self.bouton = tk.Button(self, text='Imprimer saisie',
                                command=self.imprimer_saisie)
        self.bouton.pack()

    def creer_ligne_sasie(self):
        self.texte = tk.StringVar()
        self.ligne_saisie = tk.Entry(self, textvariable=self.texte,
                                     width=30)
        self.ligne_saisie.pack()


fenetre = tk.Tk()
app = Application(master=fenetre)
app.mainloop()
