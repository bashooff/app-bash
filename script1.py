from flask import Flask, render_template

# instantiating flask object
app = Flask(__name__)

# create buttons for html pages
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/photos/")
def photos():
    return render_template("photos.html")


if __name__ == "__main__":
    app.run(debug=True)
