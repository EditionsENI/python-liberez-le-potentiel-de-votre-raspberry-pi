import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.creer_boutons_radio()
        self.pack()

    def creer_boutons_radio(self):
        self.sel_bouton_radio = tk.StringVar()
        self.bouton_radio_1 = tk.Radiobutton(self, text='Radio 1',
                                             value='Radio 1',
                                             variable=self.sel_bouton_radio,
                                             command=self.imprimer_choix)
        self.bouton_radio_2 = tk.Radiobutton(self, text='Radio 2',
                                             value='Radio 2',
                                             variable=self.sel_bouton_radio,
                                             command=self.imprimer_choix)
        self.bouton_radio_3 = tk.Radiobutton(self, text='Radio 3',
                                             value='Radio 3',
                                             variable=self.sel_bouton_radio,
                                             command=self.imprimer_choix)

        self.bouton_radio_1.pack()
        self.bouton_radio_2.pack()
        self.bouton_radio_3.pack()

        self.bouton_radio_1.select()

    def imprimer_choix(self):
        print(self.sel_bouton_radio.get() + " sélectionné")


fenetre = tk.Tk()
app = Application(master=fenetre)
app.mainloop()
