from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method=['POST']>
            
            <label>Rotate by:<input name="rot" type="test" value="0" /></label>
            <textarea name="text"></textarea>
            <input name="submit_message" type="submit" />
            
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route('/', methods=['POST'])
def handle_encrypt():
    rotnum = int(request.form["rot"])
    message = str(request.form["text"])
    encrypted_string = str(rotate_string(message,rotnum))
    return "<h1>" + encrypted_string + "</h1>"

app.run()