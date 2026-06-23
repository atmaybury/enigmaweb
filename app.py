from flask import Flask, render_template, request, jsonify
from enigma import Enigma

app = Flask(__name__)

ROTOR_COUNT = 3


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        plaintext = request.form.get("plaintext")
        if plaintext is None:
            raise Exception("No plaintext")

        # TODO: make rotor amount dynamic
        rotorPos: list[int] = []

        for i in range(ROTOR_COUNT):
            x = request.form.get("r%d" % i)
            if x:
                pos = ord(x.upper()) - 65
                rotorPos.append(pos)

        enigma = Enigma(rotorPos)

        return jsonify({"ciphertext": enigma.encipher(plaintext)})

    else:
        return render_template("index.html", ciphertext="")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
