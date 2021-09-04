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
