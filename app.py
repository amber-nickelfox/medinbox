from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('index.html')

@socketio.on('message')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print(json)
    socketio.emit('event-response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)
