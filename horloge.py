import tkinter as tk
import time 
root = tk.Tk()
root.title('Horloge')
root.geometry("400x200")
root.resizable(False, False)
root.update_idletasks()
root.overrideredirect(1)
root.attributes("-alpha", 0.5)


def horloge():
    time_ = time.strftime("%H : %M : %S %p")
    my_label.config(text=time_)
    my_label.after(1000, horloge)

def date():
    jour = time.strftime("%d")
    mois = time.strftime("%m")
    annee = time.strftime("%y")

    my_label2.config(text= jour + "-" + mois + "-" + annee )
    my_label2.after(1000, date)

def update():
    my_label.config(text="Heure")

my_label = tk.Label(root, text='', font=("Helvetica", 48), fg= "green", bg="black")
my_label.pack(pady=20)
my_label2 = tk.Label(root, text='', font=("Helvetica", 48), fg= "green", bg="black")
my_label2.pack(anchor="center")
def click(event):
    root.destroy()

root.bind("<Double-Button-1>", click)

horloge()
date()
my_label.after(1000, update)

root.mainloop()