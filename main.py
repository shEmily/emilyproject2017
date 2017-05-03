# -*- coding: utf-8 -*-
from __future__ import print_function
import json
from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

firstMenu = ["인사"]
 
#메시지
@app.route("/message", methods=['GET', 'POST'])
def message():
    userRequest = json.loads(request.get_data())


    if userRequest['content'] == u"인사":
        return """{"message": {"text":" 안녕 난 에밀리야"},"keyboard":\
  {      "type": "buttons","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""
 
    else:
        return """{"message": {"text":" 미안.. 아직 개발단계라서..."},"keyboard": {  "type": "buttons","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""


@app.route("/keyboard", methods=['GET', 'POST'])
def key():
    return """{ "type" : "buttons", "buttons" : """+'["'+'","'.join(firstMenu)+'"]'+"""}"""
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
