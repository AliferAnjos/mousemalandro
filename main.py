from tkinter import *
import random
import pyautogui as pg
import time


screen = Tk()
screen.title("Mouse Malandro")
screen.geometry("400x400")
screen.config(bg="#222222")
screen.resizable(False, False)


logo = PhotoImage(width=350, height=350, file="mickey.png")
foto = Label(image=logo)
foto.place(x=23, y=25)


global RUNNING
RUNNING = True


def start():
    global RUNNING
    RUNNING = True
    play = Button(bg="#0e1b29", fg="white", text="RUNNING", height=5, width=10, font="Consolas")
    play.place(x=50, y=250)
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
    play.place(x=50, y=250)
    kill = Button(bg="#0e1b29", fg="white", text="STOP", height=5, width=10, font="Consolas")
    kill.place(x=250, y=250)
    screen.update()
    time.sleep(1)
    screen.update()
    kill = Button(bg="#800000", fg="white", text="STOP", height=5, width=10, font="Consolas", command=stop)
    kill.place(x=250, y=250)
    return

play = Button(bg="#556b2f", fg="white", text="START", height=5, width=10, font="Consolas", command=start)
play.place(x=50, y=250)

kill = Button(bg="#800000", fg="white", text="STOP", height=5, width=10, font="Consolas", command=stop)
kill.place(x=250, y=250)


screen.mainloop()
