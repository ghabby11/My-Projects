from flask import Flask,render_template
import requests

app = Flask(__name__)


url = "https://api.npoint.io/49ca5f4bfbef381138d6"
response = requests.get("https://api.npoint.io/49ca5f4bfbef381138d6")


@app.route("/")
def home():
    data = response.json()
    print(data)
    return render_template("index.html", data=data)

@app.route("/about")
def about():
    return  render_template("about.html")

@app.route("/contact")
def contact():
    return  render_template("contact.html")

@app.route("/post/<int:number>")
def get_post(number):
    requested_post = None
    data = response.json()
    for post in data:
        if post["id"]== number:
            requested_post= post
    return render_template("post.html", post=requested_post)








if __name__ == "__main__":
    app.run(debug=True)