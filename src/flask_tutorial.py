from flask import Flask, redirect, url_for, render_template #Import Flask from library

app = Flask(__name__) #Create Flask object

@app.route("/<name>")
def home(name): #can be defined as anything, this is just our main page being displayed
    return render_template("index.html")

if __name__ == '__main__': #Safety check
    app.run()