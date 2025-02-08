from flask import Flask, render_template, request, jsonify
from enigma import enigma

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        plaintext = request.form.get('plaintext')

        # TODO: make rotor amount dynamic
        rotors = 3
        rotorPos = []

        for i in range(rotors):
            x = request.form.get("r%d" % i)
            if (x):
                pos = ord(x.upper()) - 65
                rotorPos.append(pos)

        ciphertext = enigma(plaintext, rotorPos)
        return jsonify({ "ciphertext": ciphertext })

    else:
        return render_template("index.html", ciphertext="")


@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
