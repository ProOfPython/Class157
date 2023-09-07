from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('Dictionary')
root.geometry('400x400')
root.configure(background = 'snow')

entCard = Entry(root)
entCard.place(relx = 0.5, rely = 0.4, anchor = CENTER)

def checkCard(card):
    try:
        cardInt = int(card)
    except ValueError:
        messagebox.showerror('Error!', 'Invalid Credit Card')
        return ()

    if cardInt == 2357:
        messagebox.showinfo('Info', 'Credit Card Accepted')
    else:
        messagebox.showinfo('Info', 'Credit Card Denied')

btnGetDef = Button(root, text = 'Check Credit Card', command = lambda: checkCard(entCard.get()))
btnGetDef.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()