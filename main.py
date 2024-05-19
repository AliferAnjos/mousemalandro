from tkinter import *
import random
import pyautogui as pg
import time


screen = Tk()
screen.title("Mouse Malandro")
screen.geometry("400x400")
screen.config(bg="#080808")
screen.resizable(False, False)


logo = PhotoImage(width=350, height=350, file="mickey.png")

foto = Label(image=logo)
foto.place(x=23, y=25)



def start():
        MALANDRAGEM = True
        play = Button(bg="#0e1b29", fg="white", text="RUNNING", height=5, width=10, font="Consolas")
        play.place(x=50, y=250)
        
            
        while MALANDRAGEM:

            screen.update()
            xcor = random.randint(200, 800)
            ycor = random.randint(200, 600)
            time.sleep(5)

            pg.moveTo(xcor, ycor)


            stop = Button(bg="#800000", fg="white", text="STOP", height=5, width=10, font="Consolas", command=break)
            stop.place(x=220, y=250)

            play = Button(bg="#556b2f", fg="white", text="START", height=5, width=10, font="Consolas", command=start)
            play.place(x=50, y=250)
                


def stop():
    play = Button(bg="#556b2f", fg="white", text="START", height=5, width=10, font="Consolas", command=start)
    play.place(x=50, y=250)
    screen.destroy()


play = Button(bg="#556b2f", fg="white", text="START", height=5, width=10, font="Consolas", command=start)
play.place(x=50, y=250)

stop = Button(bg="#800000", fg="white", text="STOP", height=5, width=10, font="Consolas", command=stop)
stop.place(x=220, y=250)



screen.mainloop()