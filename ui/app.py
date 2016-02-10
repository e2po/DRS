from flask import Flask
from flask_socketio import SocketIO, emit, disconnect

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def main():
    return app.send_static_file("index.html")


@socketio.on('connect', namespace='/test')
def test_connect():
    print("Client connected")
    emit('my response', {'data': 'Successfully connected'})


@socketio.on('disconnect request', namespace='/test')
def disconnect_request():
    print("Disconnect request received")
    emit('my response',
         {'data': 'Disconnected!'})
    disconnect()


@socketio.on('my event', namespace='/test')
def test_message(message):
    print(message)
    emit('my response', {'data': 'got it!'})

app.debug = True

if __name__ == '__main__':
    socketio.run(app)
    # app.run()
