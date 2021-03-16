from flask import Flask, render_template      

app = Flask(__name__)

@app.route('/<name>')
def generateResponse(name):
    if name.isupper() and name.isalpha():
        name = name.lower()
    elif name.islower() and name.isalpha():
        name = name.upper()
    else: name = ''.join([i for i in name if not i.isdigit()])
    return '<h1>Hey {}, welcome to our CSCB20 website!</h1>'.format(name)


if __name__ == '__main__':
    app.run()