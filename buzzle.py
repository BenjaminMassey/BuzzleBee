from flask import Flask, render_template, request
from tkinter import *
import threading
import time

app = Flask(__name__)

players = []

@app.route('/', methods = ['GET', 'POST'])
def index():
	global players
	try:
		result = request.form.get('name')
	except:
		result = None
	print("Here is the result:", result)
	if result is not None and result not in players:
		players.append(result)
	page = None
	try:
		page = render_template("index.html")
	except:
		print("!COULD NOT RENDER TEMPLATE!")
		page = "Unknown Error"
	return page

def SiteLoop():
	if __name__ == '__main__':
		app.run(host='127.0.0.1', port=8000)

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