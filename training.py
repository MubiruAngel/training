from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/views")
def views():
    return render_template("views.html")

@app.route("/auth")
def auth():
    return render_template("auth.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")                 




if __name__==("__main__"):
    app.run(debug=True)
