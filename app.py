from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

messages = [] 

@app.route("/")
def index():
    return render_template("chat.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username")
    text = request.form.get("text")
    if username and text:
        messages.append({"username": username, "text": text})
    return redirect(url_for("index"))

@app.route("/clear")
def clear():
    messages.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
