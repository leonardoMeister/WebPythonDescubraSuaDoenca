from flask import Flask

app = Flask(__name__)

@app.route("/")
def rotaHome():
    return "<h1> Hello word </h1>" , 200


if __name__ == "__main__":
    app.run(debug=True , port= 5000)