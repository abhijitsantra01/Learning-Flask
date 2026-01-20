from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!!'

@app.route("/about")
def about():
    return "This is my about page"

@app.route("/form", methods = ['GET','POST'])
def form():
    if request.method == "POST":
        return "You have submitted the form"
    else:
        return "You're just viewing the form"

if __name__ == "__main__":
    app.run(debug=True)
