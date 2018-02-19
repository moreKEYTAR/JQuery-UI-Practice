from flask import Flask, request, render_template

app = Flask(__name__)

app.secret_key = 'every day we practicin yeah'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/record-color', methods=["POST"])
def record_color_vote():
    color = request.form.get("colorPick")
    print color
    # update database that doesn't exist
    return color

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
