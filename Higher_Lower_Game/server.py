from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

random_number = random.randint(0,9)
print(random_number)
@app.route("/<int:number>")
def number_too_low(number):
    if int(number)< random_number:
        return '<h1 style= "color:red" "text-align:center">Too Low</h1>'\
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGF1NzE3aG1ja2hxMXJuaWFyMnlpNmltZDVxb3Mya3plZmczYWNxZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d2lcHJTG5Tscg/200.webp">'
    elif int(number)> random_number:
        return '<h1 style= "color:blue" "text-align:center">Too High</h1>'\
               '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWpjbTFzMmxvdWh3bHlubWg1eHZjd3BsNG1rMGVhY3loYXFvZGJ6MiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/KpAPQVW9lWnWU/200.webp">'
    elif int(number) == random_number:
        return '<h1 style= "color:green" "text-align:center">Correct</h1>'\
               '<img src= " https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXMwMGdpNXJjd28zbzE3OWE4ZHd5ZTFzZnIyN2JjNXB3NjJvbTJqZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/26tknCqiJrBQG6bxC/200.webp">'







if __name__ == "__main__":
    app.run(debug=True)
