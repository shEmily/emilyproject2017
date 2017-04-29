# -*- coding: utf-8 -*-

############Module import############
from __future__ import print_function
import json
from flask import Flask, request

############Module import############
 
app = Flask(__name__)
 
firstMenu = ["인사"]
 
@app.route("//message", methods=['GET', 'POST'])
@app.route("/message", methods=['GET', 'POST'])
def message():
    userRequest = json.loads(request.get_data())
 
##메시지부분 예시
    if userRequest['content'] == u"인사":
        return """{"message": {"text":" 안녕 난 에밀리야."},"keyboard":\
  {      "type": "buttons","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""
 
   
    else:
        return """{"message": {"text":" 미안 아직 개발중이라.."},"keyboard": {  "type": "buttons","buttons": """+'["'+'","'.join(firstMenu)+'"]'+""" }}"""
 
 
 
 
@app.route("//keyboard", methods=['GET', 'POST'])
@app.route("/keyboard", methods=['GET', 'POST'])
def key():
    return """{ "type" : "buttons", "buttons" : """+'["'+'","'.join(firstMenu)+'"]'+"""}"""
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

