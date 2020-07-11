from tkinter import *
import threading

root = Tk()


# my_label_1 = Label(root, text="play human vs human")
# my_label_2 = Label(root, text="play ai vs ai")
# my_label_3 = Label(root, text="play human vs ai")

# my_label_1.grid(row=0, column=0)
# my_label_2.grid(row=1, column=0)
# my_label_3.grid(row=2, column=0)

def play():
    import Window


def click_button_1():
    t = threading.Thread(target=play)
    t.start()
    print("od kliknieto")
    return 0


my_button_1 = Button(root, text="play human vs human", command=click_button_1, pady=50)
my_button_2 = Button(root, text="play ai vs ai", pady=50)
my_button_3 = Button(root, text="play human vs ai", pady=50)
my_button_1.grid(row=0, column=0)
my_button_2.grid(row=1, column=0)
my_button_3.grid(row=2, column=0)

root.mainloop()
