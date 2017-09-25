from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
        form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px
        }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>      
    </head>
    <body>
      <form method='post'>

        <label>Rotate by:<input name="rot" type="test" value="0" /></label>
        <textarea name="text">{0}</textarea>
        <input name="submit message" type="submit" />

      </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route('/', methods=['POST'])
def encrypt():
    rotnum = request.form.get("rot")
    rotnum = int(rotnum)
    message = request.form.get("text")
    message = str(message)
    encrypted_string = str(rotate_string(message,rotnum))
    return form.format(encrypted_string)

app.run()