import logging
import time
import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

import psutil


class TextHandler(logging.Handler):

    def __init__(self, widget_text):
        super(TextHandler, self).__init__()
        self.widget_text = widget_text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.widget_text.configure(state='normal')
            self.widget_text.insert(tk.END, msg + '\n')
            self.widget_text.configure(state='disabled')
            self.widget_text.yview(tk.END)

        self.widget_text.after(0, append)


class Application(tk.Frame):

    def __init__(self, master):
        super(Application, self).__init__(master=master)
        self.build_gui()

    def build_gui(self):

        self.grid(column=0, row=0, sticky='ew')
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        self.log_widget = ScrolledText(self, state='disabled')
        self.log_widget.grid(column=0, row=1, sticky='w', columnspan=4)

        text_handler = TextHandler(self.log_widget)
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        logger.addHandler(text_handler)


def worker():
    while True:
        time.sleep(1)
        msg = ''
        for cpu_idx, cpu_info in enumerate(psutil.cpu_freq(percpu=True)):
            msg = msg + 'CPU {}: {} Hz \n'.format(cpu_idx, cpu_info.current)
        logging.info(msg)


fenetre = tk.Tk()
Application(fenetre)
t1 = threading.Thread(target=worker, args=[])
t1.start()
fenetre.mainloop()
t1.join()
