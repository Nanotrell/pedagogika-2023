from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/quotes")
def quotes():
	return render_template("quotes.html")

@app.route("/sourse")
def sourse():
	return render_template("sourse.html")

@app.route("/books")
def books():
	return render_template("books.html")

if __name__ == '__main__' :
	app.run(debug=True)
