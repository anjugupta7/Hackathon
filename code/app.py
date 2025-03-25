from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        user_input = request.form.get("user_input")
        output = f"You entered: {user_input}"  # Modify this to process input as needed
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)