from flask import Flask, render_template, request
from tkinter import *
import threading
import time
import math

app = Flask(__name__)

players = dict() # string player -> (int score, bool active, float time)

start_time = time.time()

point_amount = 200

@app.route('/', methods = ['GET', 'POST'])
def index():
    global players, start_time
    result = None
    try:
        result = request.form.get('name')
    except:
        print("WARNING: no name - either new or failure")
    if result is not None:
        if result not in players:
            players[result] = (0, False)
        else:
            players[result] = (players[result][0], True, time.time() - start_time)
    
    player_text = result if result is not None else ""
    page = None
    try:
        page = render_template("index.html", player_name=player_text)
    except:
        print("ERROR: could not render index.html")
        page = "Unknown Error"
    return page

try:
    with open("address.txt", "r") as address_file:
        address = address_file.read()
except:
    address = "127.0.0.1:80"
    with open("address.txt", "w") as address_file:
        address_file.write(address)

def SiteLoop():
    global address
    fields = address.split(':')
    host = fields[0]
    if len(fields) > 1:
        port = int(fields[1])
    else:
        port = 80
    if __name__ == '__main__':
        app.run(host=host, port=port)

window = Tk()
window.title("Buzzle Bee")
window.geometry('600x900')

def GuiLoop():
    global window, players, start_time, point_amount
    
    def Reset():
        global players, start_time
        for player in players.keys():
            players[player] = (players[player][0], False)
        start_time = time.time()

    def Winner(me):
        global players, point_amount
        players[me] = (players[me][0] + point_amount, False)
        Reset()

    def Loser(me):
        global players, point_amount
        players[me] = (players[me][0] - point_amount, False)
    
    reset_button = Button(window, text="Reset", command=Reset)
    reset_button.config(font=("Courier", 18))
    reset_button.pack(pady=20)

    green_text = StringVar()
    green_text.set("")
    green_label = Label(window, textvariable=green_text, wraplength=600, fg="#009700")
    green_label.config(font=("Courier", 24))
    green_label.pack()

    text = StringVar()
    text.set("")
    label = Label(window, textvariable=text, wraplength=600)
    label.config(font=("Courier", 24))
    label.pack()

    points = StringVar()
    points.set(str(point_amount))
    point_entry = Entry(window, textvariable=points)
    point_entry.config(font=("Courier", 14), width=8)
    point_entry.pack(pady=(0,20))

    created = ""

    while True:
        info = []
        for player in players.keys():
            if player not in created:
                win = Button(window, text=player+" Win", command=lambda x=player: Winner(x), bg="#FFD700")
                win.config(font=("Courier", 16))
                win.pack()
                lose = Button(window, text=player+" Lose", command=lambda x=player: Loser(x), bg="#8B0000")
                lose.config(font=("Courier", 10))
                lose.pack()
                created += player
            piece = player + ": " + str(players[player][0])
            if players[player][1]:
                piece += " [" + str(round(players[player][2], 3)) + "]"
                info.append((players[player][0], players[player][2], piece))
            else:
                info.append((players[player][0], math.inf, piece))
        info = sorted(info, key=lambda x: x[0])
        info = reversed(info)
        info = sorted(info, key=lambda x: x[1])
        green = ""
        non_green = ""
        for pieces in info:
            if pieces[1] == math.inf:
                non_green += pieces[2] + "\n"
            else:
                green += pieces[2] + "\n"
        green_text.set(green)
        text.set(non_green)
        try:
            point_amount = int(points.get())
        except:
            point_amount = 0
        time.sleep(0.05)

site = threading.Thread(target=SiteLoop)
site.start()

gui = threading.Thread(target=GuiLoop)
gui.start()

window.mainloop()
