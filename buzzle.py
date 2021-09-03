from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
	try:
		result = request.form.get('name')
	except:
		result = None
	print("Here is the result:", result)
	page = None
	try:
		page = render_template("index.html")
	except:
		print("!COULD NOT RENDER TEMPLATE!")
		page = "Unknown Error"
	return page

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)