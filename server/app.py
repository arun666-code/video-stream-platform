import os
import sqlite3
from flask import Flask, request, jsonify, send_file, abort, send_from_directory, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'videos')
CLIENT_FOLDER = os.path.join(app.root_path, '..', 'client')
DATABASE = os.path.join(app.root_path, 'videos.db')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            'CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT)'
        )


def add_video(filename: str):
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.execute('INSERT INTO videos (filename) VALUES (?)', (filename,))
        conn.commit()
        return cur.lastrowid


def get_videos():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.execute('SELECT id, filename FROM videos')
        return [{'id': row[0], 'filename': row[1]} for row in cur.fetchall()]


@app.route('/')
def root():
    return send_from_directory(CLIENT_FOLDER, 'index.html')


@app.route('/client/<path:path>')
def client_files(path):
    return send_from_directory(CLIENT_FOLDER, path)


@app.route('/api/videos')
def api_videos():
    return jsonify(get_videos())


@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'}), 400
    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    add_video(filename)
    return jsonify({'message': 'uploaded'}), 201


@app.route('/video/<path:filename>')
def stream_video(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.isfile(file_path):
        abort(404)

    range_header = request.headers.get('Range', None)
    if not range_header:
        return send_file(file_path, mimetype='video/mp4')

    size = os.path.getsize(file_path)
    byte1, byte2 = 0, None

    m = range_header.replace('bytes=', '').split('-')
    if len(m) == 2:
        if m[0]:
            byte1 = int(m[0])
        if m[1]:
            byte2 = int(m[1])
    length = size - byte1
    if byte2 is not None:
        length = byte2 - byte1 + 1
    data = None
    with open(file_path, 'rb') as f:
        f.seek(byte1)
        data = f.read(length)
    rv = app.response_class(data,
                             status=206,
                             mimetype='video/mp4',
                             direct_passthrough=True)
    rv.headers.add('Content-Range', f'bytes {byte1}-{byte1 + length - 1}/{size}')
    return rv


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
