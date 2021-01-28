from flask import Flask, render_template, request, redirect
from gtts import gTTS
import os

app = Flask(__name__)


def read_File(file):
    f = open(file, "r")
    x = f.read()

    audio = gTTS(text=x, lang='tr', slow=False)
    audio.save("deneme.mp3")
    os.system('open deneme.mp3')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        req = request.form
        file = req["file_input"]
        read_File(file)
        return redirect(request.url)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=8836, debug=True)

#flask run

