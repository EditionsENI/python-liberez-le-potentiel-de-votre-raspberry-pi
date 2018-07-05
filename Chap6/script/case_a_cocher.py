import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.creer_cases_a_cocher()
        self.pack()

    def imprimer_choix(self):
        print('Choix 1 est selectionne : ' + str(self.sel_choix.get()))

    def creer_cases_a_cocher(self):
        self.sel_choix = tk.BooleanVar()
        self.choix = tk.Checkbutton(self, text="Choix 1",
                                    variable=self.sel_choix,
                                    command=self.imprimer_choix)
        self.choix.pack()


fenetre = tk.Tk()
app = Application(master=fenetre)
app.mainloop()
