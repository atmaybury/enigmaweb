from flask import Flask, render_template, request
from enigma import enigma

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        plaintext = request.form.get("plaintext")
        r1 = int(request.form.get("r1"))
        r2 = int(request.form.get("r2"))
        r3 = int(request.form.get("r3"))
        ciphertext = enigma(plaintext, r1, r2, r3)
        return render_template("index.html", ciphertext=ciphertext)

    if request.method == "GET":
        return render_template("index.html", ciphertext="")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
