from tkinter import *

tk = Tk()
win = tk
win.title("Tic Tac Toe by Vinay")
win.geometry("800x800")

# Top frame setup
frame_top = LabelFrame(win, padx=40, pady=40)
frame_top.pack(padx=20, pady=20)

def easy():
    import ticrandom

def medium():
    import ticmedium

def hard():
    import tichard

label = Label(frame_top, text="Select Level.").grid(row=0, column=2)

player_button_1 = Button(frame_top, text="Easy", height=3, width=6, command=easy).grid(row=1, column=0)
player_button_2 = Button(frame_top, text="Medium", height=3, width=6, command=medium).grid(row=1, column=2)
player_button_3 = Button(frame_top, text="Hard", height=3, width=6, command=hard).grid(row=1, column=6)

Button(win, text='Exit',command=lambda:win.destroy(),height=5,width=10).pack(expand=True)
win.mainloop()