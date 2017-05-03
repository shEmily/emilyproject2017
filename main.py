# -*- coding: utf-8 -*-
#utf-8인코딩선언

#from 모듈  import 클래스 (모듈에 있는 클래스 임포트 시킴)
from __future__ import print_function
import json
from flask import Flask, request

app = Flask(__name__)   #플라스크 애플리케이션의 모듈명을 Flask 클래스의 첫번째 인자로 넘겨주며 플라스크 애플리케이션 객체인 "app"을 생성한다. 이 플라스크 객체로 모든 플라스크 기능을 사용할 수 있다.
app.config['DEBUG'] = True  #디버깅 모드 온-트루, 오프 폴스

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

#특정 URL을 호출했을 때 호출되는 함수를 정의한다. 요청에 대한 응답 == view함수. 특정 URI와 일치시키기 위해 플라스크에서 미리 정의한 route() 데코레이터를 사용한다. /message를 호출했을 때 message()함수가 실행 됨.
#키보드
@app.route("https://emilyproject2017.appspot.com/keyboard", methods=['GET'])
def keyboard():
    key = {
        "type" : "buttons",
        "buttons" : [u"A", u"B", u"C"]
    }



#메시지
@app.route("https://emilyproject2017.appspot.com/message", methods=['POST'])
def message():
    message = [
    {
        "message":{
            "text" : "Apple"
        },
        "keyboard" : {
            "type" : "buttons",
            "buttons" : [
                u"A",
                u"B",
                u"C"
            ]
        }
    },
    {
        "message":{
            "text" : "Banana"
        },
        "keyboard" : {
            "type" : "buttons",
            "buttons" : [
                u"A",
                u"B",
                u"C"
            ]
        }
    },
    {
        "message":{
            "text" : "Cherry"
        },
        "keyboard" : {
            "type" : "buttons",
            "buttons" : [
                u"A",
                u"B",
                u"C"
            ]
        }
    },
    {
        "message":{
            "text" : "이건 뭐야?",
            "message_button" : {
                "label" : "홈페이지로",
                "url" : "http://www.shinhan.ac.kr/"
            }
        }
    }
    ]
    
#친구추가
@app.route("https://emilyproject2017.appspot.com/friend", methods=['POST'])
def friend():
    friend = { 
        "user_key" : "HASHED_USER_KEY",
        "message" : "친구추가 감사합니다!"
    }
    
#친구삭제
@app.route("https://emilyproject2017.appspot.com/friend/:user_key", methods=['DELETE'])
def friend():
    friend = { "message" : "아쉽지만.. 다음에 또 만나길 바래요!"}
    
#채팅방 나가기
@app.route("https://emilyproject2017.appspot.com/chat_room/HASHED_USER_KEY", methods=['DELETE'])
def chat_room():
    chat_room = { "message" : "여전히 공지는 받으실 수 있어요!"}

    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
