from flask import Flask, render_template, request, jsonify
from flask_jsglue import JSGlue
from enigma import enigma

app = Flask(__name__)
jsglue = JSGlue(app)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        plaintext = request.form["plaintext"]
        
        # TODO: make rotor amount dynamic
        rotors = 3
        rotorPos = []

        for i in range(rotors):
            x = request.form["r%d" % i]
            pos = ord(x.upper()) - 65
            rotorPos.append(pos)

        ciphertext = enigma(plaintext, rotorPos)

        return jsonify({ "ciphertext":ciphertext })

    if request.method == "GET":
        return render_template("index.html", ciphertext="")


@app.route("/about")
def about():
    
    return render_template("about.html")

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.run()
