from flask import Flask
import random

rand_num = random.randint(0, 9)
print(rand_num)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHQwbWp5Z3FiZ24zMTh1bzN6OHZvbW56ZnNxeDN2a2FqcG5rNWk1MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/glJdAXojfP3wPEg84a/giphy.gif'/>"


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > rand_num:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnZvbm9hdWFqemQzeHg4bml2b3MxZ3Z0YTZrZ2V6Y3pmeGo1MXlsbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7btPitD723wPmVsk/giphy.gif'/>"

    elif guess < rand_num:
        return "<h1 style='color: blue'>Too low, try again!</h1>"\
               "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDIxMnlvdGRqandlamVlOXdxZHpvdHlobWNnZXV6d3BleGFmdHA0cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Wu7UDoOBHPHm8/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYjQwZDlhMG44cW50MjJ2OHBjd3A1bjZmYW5jdnlrMHM5MHRuZ2k0NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ic91gaFqsYXG8/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
