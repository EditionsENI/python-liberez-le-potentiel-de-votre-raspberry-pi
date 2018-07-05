import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.creer_bouton()
        self.pack()

    def imprimer_bonjour(self):
        print("Bonjour!!!")

    def creer_bouton(self):
        self.bouton = tk.Button(self, text='Imprimer texte',
                                command=self.imprimer_bonjour)
        self.bouton.pack()


fenetre = tk.Tk()
app = Application(master=fenetre)
app.mainloop()
