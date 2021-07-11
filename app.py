from flask import Flask, request
import json
import google_actions as actions
from alexa import alexa_app

app = Flask(__name__)


app.register_blueprint(alexa_app,url_prefix="/alexa")


###google endpoint

@app.route('/google')
def webhook():
    return actions.action(request)


   
if __name__ == '__main__ ':
    app.run(debug=True)
