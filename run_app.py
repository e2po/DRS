"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""
from drs.ui.app import app, socketio

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
