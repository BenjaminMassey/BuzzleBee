from flask import Flask, render_template, request
from tkinter import *
import threading
import time

app = Flask(__name__)

players = []

@app.route('/', methods = ['GET', 'POST'])
def index():
	global players
	result = None
	try:
		result = request.form.get('name')
	except:
		print("WARNING: no name - either new or failure")
	if result is not None and result not in players:
		players.append(result)
	player_text = result if result is not None else ""
	page = None
	try:
		page = render_template("index.html", player_name=player_text)
	except:
		print("ERROR: could not render index.html")
		page = "Unknown Error"
	return page

try:
	address_file = open("address.txt", "r")
	address = address_file.read()
	address_file.close()
except:
	address_file = open("address.txt", "w")
	address = "127.0.0.1"
	address_file.write(address)
	address_file.close()

def SiteLoop():
	global address
	if __name__ == '__main__':
		app.run(host=address, port=80)

window = Tk()
window.title("Buzzle Bee")
window.geometry('300x600')

def GuiLoop():
	global window, players
	
	def Reset():
		global players
		players = []
	button = Button(window, text="Reset", command=Reset)
	button.config(font=("Courier", 24))
	button.pack()
	
	text = StringVar()
	text.set("")
	label = Label(window, textvariable=text, wraplength=300)
	label.config(font=("Courier", 24))
	label.pack()
	
	while True:
		queue = ""
		for player in players:
			queue += player + "\n"
		text.set(queue)
		time.sleep(0.05)

site = threading.Thread(target=SiteLoop)
site.start()

gui = threading.Thread(target=GuiLoop)
gui.start()

window.mainloop()