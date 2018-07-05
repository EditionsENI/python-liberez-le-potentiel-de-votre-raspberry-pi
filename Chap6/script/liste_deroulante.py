import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super(Application, self).__init__(master=master)
        self.creer_liste_deroulante()
        self.creer_bouton()
        self.pack()

    def creer_liste_deroulante(self):
        self.items = tk.StringVar(
            value=['Element 1', 'Element 2', 'Element 3'])
        self.liste_deroulante = tk.Listbox(self, listvariable=self.items,
                                           selectmode='multiple')
        self.liste_deroulante.insert(tk.END, 'Element 4')
        self.liste_deroulante.pack()

    def imprimer_element_selectionne(self):
        element_idx = self.liste_deroulante.curselection()
        if element_idx:
            print('Element selectionne:')
            for elt in element_idx:
                print('\t' + self.liste_deroulante.get(elt))
        else:
            print('No element selectionne')

    def creer_bouton(self):
        self.bouton = tk.Button(self, text='Imprimer element selectione',
                                command=self.imprimer_element_selectionne)
        self.bouton.pack()


fenetre = tk.Tk()
app = Application(master=fenetre)
app.mainloop()
