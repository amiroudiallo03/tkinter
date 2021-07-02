git #simple calculator
import tkinter as tk
from tkinter import RIGHT, END, DISABLED, NORMAL

#fenetre
root = tk.Tk()
root.title('calculatrice')
root.geometry('200x300')
root.resizable(False,False)

#definit couleur et le font

dark_green = '#93af22'
light_green = '#acc253'
white_green = '#edefe0'
button_font = ('Arial', 20)
display_font = ('Arial', 30)

#funtion
def submit_number(number):
    """ add number"""
    display.insert(END, number)

    if "." in display.get():
        decimal_button.config(state=DISABLED)

def operate(operator):
    global first_number
    global operation 

    operation = operator
    first_number = display.get()

    display.delete(0, END)

    add_button.config(state=DISABLED)  
    subtract_button.config(state=DISABLED)  
    multiply_button.config(state=DISABLED)  
    divide_button.config(state=DISABLED)  
    exponent_button.config(state=DISABLED)  
    inverse_button.config(state=DISABLED)  
    square_button.config(state=DISABLED)

    decimal_button.config(state=NORMAL)

def equal():
    if operation == 'add':
        value = float(first_number) + float(display.get())
    elif operation == 'subtract':
        value = float(first_number) - float(display.get())
    elif operation == 'multiply':
        value = float(first_number) * float(display.get())
    elif operation == 'divide':
        if display.get() == "0":
            value = 'ERROR'
        else:
            value = float(first_number) / float(display.get())
    elif operation == 'exponent':
        value = float(first_number) ** float(display.get())

    display.delete(0, END)
    display.insert(0, value)

    enable_buttons()

def enable_buttons():

    decimal_button.config(state=NORMAL)
    add_button.config(state=NORMAL)  
    subtract_button.config(state=NORMAL)  
    multiply_button.config(state=NORMAL)  
    divide_button.config(state=NORMAL)  
    exponent_button.config(state=NORMAL)  
    inverse_button.config(state=NORMAL)  
    square_button.config(state=NORMAL)

def clear():
    display.delete(0, END)

    enable_buttons()

def inverse():
    if display.get() == "0":
        value = "ERROR"
    else:
        value = 1/float(display.get())

    display.delete(0, END)
    display.insert(0,value)

def square():
    
    value = float(display.get()) ** 2 

    display.delete(0, END)
    display.insert(0,value)

def negate():
    value = -1*float(display.get())

    display.delete(0, END)
    display.insert(0,value)

display_frame = tk.LabelFrame(root)
button_frame = tk.LabelFrame(root)
display_frame.pack(padx=2, pady=(5,20))
button_frame.pack(padx=2, pady=5)

display = tk.Entry(display_frame, width= 50, font=display_font, bg= white_green, borderwidth=5, justify=RIGHT)
display.pack(padx=5, pady=5)

clear_button = tk.Button(button_frame,text="clear", font=button_font, bg=dark_green, command=clear)
quit_button = tk.Button(button_frame,text="quit", font=button_font, bg=dark_green, command=root.destroy)

inverse_button = tk.Button(button_frame, text='1/x', font=button_font, bg=light_green, command=inverse)
square_button = tk.Button(button_frame, text='x^2', font=button_font, bg=light_green, command=square)
exponent_button = tk.Button(button_frame, text='x^n', font=button_font, bg=light_green, command=lambda:operate('exponent'))
divide_button = tk.Button(button_frame, text='÷', font=button_font, bg=light_green, command=lambda:operate('divide'))
multiply_button = tk.Button(button_frame, text='*', font=button_font, bg=light_green, command=lambda:operate('multiply'))
subtract_button = tk.Button(button_frame, text='-', font=button_font, bg=light_green, command=lambda:operate('subtract'))
add_button = tk.Button(button_frame, text='+', font=button_font, bg=light_green, command=lambda:operate('add'))
equal_button = tk.Button(button_frame, text='=', font=button_font, bg=light_green, command=equal)
decimal_button = tk.Button(button_frame, text='.', font=button_font, bg=light_green, command=lambda:submit_number("."))
negate_button = tk.Button(button_frame, text='+/-', font=button_font, bg=light_green, command=negate)

nine_button = tk.Button(button_frame,text="9", font=button_font, bg=light_green, command=lambda:submit_number(9))
height_button = tk.Button(button_frame,text="8", font=button_font, bg=light_green, command=lambda:submit_number(8))
seven_button = tk.Button(button_frame, text="7",font=button_font, bg=light_green, command=lambda:submit_number(7))
six_button = tk.Button(button_frame, text="6",font=button_font, bg=light_green, command=lambda:submit_number(6))
five_button = tk.Button(button_frame, text="5",font=button_font, bg=light_green, command=lambda:submit_number(5))
four_button = tk.Button(button_frame, text="4",font=button_font, bg=light_green, command=lambda:submit_number(4))
three_button = tk.Button(button_frame, text="3",font=button_font, bg=light_green, command=lambda:submit_number(3))
two_button = tk.Button(button_frame, text="2",font=button_font, bg=light_green, command=lambda:submit_number(2))
one_button = tk.Button(button_frame, text="1",font=button_font, bg=light_green, command=lambda:submit_number(1))
zero_button = tk.Button(button_frame, text="0",font=button_font, bg=light_green, command=lambda:submit_number(0))

#first row
clear_button.grid(row=0, column=0)
quit_button.grid(row=0, column=1)
#second row
inverse_button.grid(row=1, column=0, pady=1, sticky="WE")
square_button.grid(row=1, column=1, pady=1, sticky="WE")
exponent_button.grid(row=1, column=2, pady=1, sticky="WE")
divide_button.grid(row=1, column=3, pady=1, sticky="WE")
#third row
nine_button.grid(row=2, column=0, pady=1, sticky="WE")
height_button.grid(row=2, column=1, pady=1, sticky="WE")
seven_button.grid(row=2, column=2, pady=1, sticky="WE")
multiply_button.grid(row=2, column=3, pady=1, sticky="WE")
#four row
six_button.grid(row=3, column=0, pady=1, sticky="WE")
five_button.grid(row=3, column=1, pady=1, sticky="WE")
four_button.grid(row=3, column=2, pady=1, sticky="WE")
subtract_button.grid(row=3, column=3, pady=1, sticky="WE")
#five row
three_button.grid(row=4, column=0, pady=1, sticky="WE")
two_button.grid(row=4, column=1, pady=1, sticky="WE")
one_button.grid(row=4, column=2, pady=1, sticky="WE")
add_button.grid(row=4, column=3, pady=1, sticky="WE")
#six row
zero_button.grid(row=5, column=1, pady=1, sticky="WE")
negate_button.grid(row=5, column=0, pady=1, sticky="WE")
decimal_button.grid(row=5, column=2, pady=1, sticky="WE")
equal_button.grid(row=5, column=3, pady=1, sticky="WE")
#run
root.mainloop()
