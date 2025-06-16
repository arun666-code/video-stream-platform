import os
from flask import Flask, jsonify, send_from_directory, abort

app = Flask(__name__)
HLS_FOLDER = os.path.join(app.root_path, 'static', 'hls')
CLIENT_FOLDER = os.path.join(app.root_path, '..', 'client')

os.makedirs(HLS_FOLDER, exist_ok=True)


def get_videos():
    videos = []
    for entry in os.listdir(HLS_FOLDER):
        playlist = os.path.join(HLS_FOLDER, entry, 'index.m3u8')
        if os.path.isfile(playlist):
            videos.append({
                'id': entry,
                'filename': f'{entry}.mp4',
                'hls_path': f'/hls/{entry}/index.m3u8'
            })
    return videos


@app.route('/')
def root():
    return send_from_directory(CLIENT_FOLDER, 'index.html')


@app.route('/client/<path:path>')
def client_files(path):
    return send_from_directory(CLIENT_FOLDER, path)


@app.route('/api/videos')
def api_videos():
    return jsonify(get_videos())




@app.route('/hls/<path:path>')
def hls_files(path):
    directory = os.path.join(HLS_FOLDER, os.path.dirname(path))
    filename = os.path.basename(path)
    if not os.path.isfile(os.path.join(directory, filename)):
        abort(404)
    return send_from_directory(directory, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
