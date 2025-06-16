import os
import sqlite3
import subprocess
from flask import Flask, request, jsonify, send_from_directory, abort
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'videos')
HLS_FOLDER = os.path.join(app.root_path, 'static', 'hls')
CLIENT_FOLDER = os.path.join(app.root_path, '..', 'client')
DATABASE = os.path.join(app.root_path, 'videos.db')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(HLS_FOLDER, exist_ok=True)


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            'CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, hls_path TEXT)'
        )


def add_video(filename: str, hls_dir: str):
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.execute('INSERT INTO videos (filename, hls_path) VALUES (?, ?)', (filename, hls_dir))
        conn.commit()
        return cur.lastrowid


def get_videos():
    with sqlite3.connect(DATABASE) as conn:
        cur = conn.execute('SELECT id, filename, hls_path FROM videos')
        return [
            {'id': row[0], 'filename': row[1], 'hls_path': row[2]}
            for row in cur.fetchall()
        ]


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
    upload_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(upload_path)

    # Transcode to HLS using ffmpeg
    video_id = os.path.splitext(filename)[0]
    hls_dir = os.path.join(HLS_FOLDER, video_id)
    os.makedirs(hls_dir, exist_ok=True)
    playlist_path = os.path.join(hls_dir, 'index.m3u8')
    cmd = [
        'ffmpeg', '-i', upload_path,
        '-codec:V', 'libx264', '-codec:a', 'aac',
        '-start_number', '0',
        '-hls_time', '10',
        '-hls_list_size', '0',
        '-f', 'hls', playlist_path
    ]
    try:
        subprocess.run(cmd, check=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    add_video(filename, f'/hls/{video_id}/index.m3u8')
    return jsonify({'message': 'uploaded', 'playlist': f'/hls/{video_id}/index.m3u8'}), 201


@app.route('/hls/<path:path>')
def hls_files(path):
    directory = os.path.join(HLS_FOLDER, os.path.dirname(path))
    filename = os.path.basename(path)
    if not os.path.isfile(os.path.join(directory, filename)):
        abort(404)
    return send_from_directory(directory, filename)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
