from flask import Flask,render_template

app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/")
def login():
    return "login"

@app.route("/")
def register():
    return "register"




if __name__ == "__main__":
    app.run(debug=True)