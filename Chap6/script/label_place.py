import tkinter as tk

fenetre = tk.Tk()
fenetre.geometry('640x480')
label = tk.Label(master=fenetre, text="Hello world!!!")
label.place(x=20, y=30)
fenetre.mainloop()
