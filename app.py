from flask import Flask, render_template, request
from enigma import enigma

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        plaintext = request.form.get("plaintext")
        ciphertext = enigma(plaintext)
        return render_template("index.html", ciphertext=ciphertext)

    if request.method == "GET":
        return render_template("index.html", ciphertext="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
