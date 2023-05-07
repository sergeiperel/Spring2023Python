import time
from datetime import datetime
from flask import Flask, request, abort

app = Flask(__name__)
db = [
    {
        'time': time.time(),
        'name': 'Jack',
        'text': 'Привет, всем!',
    },
    {
        'time': time.time(),
        'name': 'Mary',
        'text': 'Привет, Jack!',

    },
]


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time': time.asctime(),
        'time2': time.time(),
        'time3': datetime.now(),
        'time4': str(datetime.now()),
        'time5': datetime.now().strftime('%Y/%y/%m/%d time: %H:%M:%S'),
        'time6': datetime.now().isoformat(),

    }


@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)
    if len(data) != 2:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str) \
            or name == '' or text == '':
        return abort(400)

    message = {
        'time': time.time(),
        'name': name,
        'text': text,
    }
    db.append(message)

    return {"OK": True}


@app.route("/messages")
def get_messages():
    # print(request.args['after'])
    # print(type(request.args['after']))
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    result = []
    for message in db:
        if message['time'] > after:
            result.append(message)
            if len(result) >= 100:
                break
    return {'messages': result}


app.run()
