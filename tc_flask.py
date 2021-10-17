from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"    

if __name__ == "__main__":
    app.run()