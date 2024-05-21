from tkinter import *
import random
import pyautogui as pg
import time
import os
import sys


base_path = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
foto = os.path.join(base_path, 'images', 'mickey.png')
icone = os.path.join(base_path, 'images', 'mick.ico')

screen = Tk()
screen.title("Mouse Malandro")
screen.geometry("400x400")
screen.config(bg="#222222")
screen.iconbitmap(icone)
screen.resizable(False, False)


logo = PhotoImage(width=350, height=350, file=foto)
foto = Label(image=logo)
foto.place(x=23, y=23)
site = Label(text="LASTDREAMER.COM", fg="white", font="Consolas", bg="#222222", width=0)
site.place(x=128, y=377)


global RUNNING
RUNNING = True


def start():
    global RUNNING
    RUNNING = True
    play = Button(bg="#0e1b29", fg="white", text="RUNNING", height=5, width=10, font="Consolas")
    play.place(x=50, y=252)
    screen.update()
                    
    while RUNNING:
        screen.update()
        xcor = random.randint(200, 800)
        ycor = random.randint(200, 600)
        time.sleep(5)
        pg.moveTo(xcor, ycor)
        if RUNNING == False:
            return
            

def stop():
    global RUNNING
    RUNNING = False

    play = Button(bg="#556b2f", fg="white", text="START", height=5, width=10, font="Consolas", command=start)
    play.place(x=50, y=252)
    kill = Button(bg="#0e1b29", fg="white", text="STOP", height=5, width=10, font="Consolas")
    kill.place(x=250, y=252)
    screen.update()
    time.sleep(1)
    screen.update()
    kill = Button(bg="#800000", fg="white", text="STOP", height=5, width=10, font="Consolas", command=stop)
    kill.place(x=250, y=252)
    return

play = Button(bg="#556b2f", fg="white", text="START", height=5, width=10, font="Consolas", command=start)
play.place(x=50, y=252)

kill = Button(bg="#800000", fg="white", text="STOP", height=5, width=10, font="Consolas", command=stop)
kill.place(x=250, y=252)


screen.mainloop()
