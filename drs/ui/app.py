"""
Authors:    Porebski Elvis      C00170343
            Tyrakowski Bartosz  C00155128
Date:       February, 2016
"""
import json

from drs.drs import Drs
from flask import Flask
from flask_socketio import SocketIO, emit

from drs.mft.record import Record
from drs.partition.ntfspartition import NtfsPartition
from drs.partition.partitionmanager import PartitionManager
from os.path import exists

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect')
def connected():
    print('Client is connected')
    emit('connection status', {'status': 'connected'})


@app.route('/')
def angular():
    return app.send_static_file('index.html')


@socketio.on('request:partitions')
def get_partitions():
    print('client requested partitions...')
    partitions = PartitionManager.load_partitions()

    response = [partition.to_json() for partition in partitions]
    print(response)
    emit('response:partitions', json.dumps(response))


@socketio.on('request:mft_analyse')
def analyse_mft(path):
    if exists(path):
        drs = Drs()

        source = None

        partitions = drs.get_partitions()
        for partition in partitions:
            if partition.path == path:
                source = partition
                break

        if source is None:
            source = NtfsPartition(path=path, size=0, label=path)

        drs.analyse(partition=source, callback=socket_callback)
        print('MFT analysis completed.')
        results = []
        for deleted_record in drs.data_bank.values():
            print(deleted_record,
                  'Record Number: {}'.format(deleted_record['data'].record_number),
                  'Size: {}'.format(deleted_record['data'].attrs['size']),
                  'File Seq NO: {}'.format(deleted_record['data'].attrs['parent_dir_file_req_no']),
                  'Parent Dir Seq NO: {}'.format(deleted_record['data'].attrs['parent_dir_seq_no']))
            file_name = deleted_record['data'].attrs['file_name']
            path = deleted_record['path']
            is_orphan = deleted_record['is_orphan']

            results.append({
                'file_name': file_name,
                'dir_path': path,
                'is_orphan': is_orphan
            })
        emit('deleted_file_found', json.dumps(results))


app.debug = True


def socket_callback(record_number, total):
    if record_number % 1000 == 0 or record_number == total:
        emit('mft_analyser_progress', {
            'current': record_number,
            'total': total
        })

if __name__ == '__main__':
    socketio.run(app)
