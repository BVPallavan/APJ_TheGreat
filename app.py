from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Dr.APJ Abdul Kalam", Designation="The Great and Scientist of India", location="he Great India")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)