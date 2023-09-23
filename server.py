from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def home():
    return (f'<html>\
                <head>\
                    <title>Guess a Number</title>\
                </head>\
                <body>\
                    <h1>Guess a number between 0 and 9</h1>\
    <iframe src="https://giphy.com/embed/4H3Ii5eLChYul9p7NL" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>\
                </body>\
            </html>')


def random_number_gen():
    ran_no = random.randint(0,9)
    return ran_no


@app.route('/<int:chosen_number>')
def user_check(chosen_number):
    # Now calling our random Number
    comp_no = random_number_gen()
    print(comp_no)
    print(chosen_number)

    if comp_no == chosen_number:

        return (f'<h1 style = "color: Green">You found me</h1>\
                <img src = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">\
        <h2> Your chosen number is {chosen_number}\n i chose {comp_no}</h2>')
    elif comp_no < chosen_number:
        return (f'<h1 style = "color: Red">Is too high</h1>\
                <img src = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">\
                <h2> Your chosen number is {chosen_number}\n while i chose {comp_no}</h2>')
    else:
        return (f'<h1 style = "color: Purple">Is too low</h1>\
                    <img src ="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" >\
                <h2> Your chosen number is {chosen_number}\n while I chose is {comp_no}</h2>')




if __name__ == '__main__':
    app.run(debug=True)
