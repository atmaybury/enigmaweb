from flask import Flask, render_template, request, jsonify
from enigma import enigma

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        plaintext = request.form.get("plaintext")
        
        # TODO: make rotor amount dynamic
        rotors = 3
        rotorPos = []

        for i in range(rotors):
            x = request.form.get("r%d" % i)
            pos = ord(x.upper()) - 65
            rotorPos.append(pos)

        ciphertext = enigma(plaintext, rotorPos)

        return render_template("index.html", ciphertext=ciphertext)

    if request.method == "GET":
        return render_template("index.html", ciphertext="")

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run()
