from flask import Flask, render_template, send_file, request, abort
import os

app = Flask(__name__)

VIDEO_DIR = os.path.join(app.root_path, 'static', 'videos')

@app.route('/')
def index():
    videos = [f for f in os.listdir(VIDEO_DIR) if f.lower().endswith('.mp4')]
    return render_template('index.html', videos=videos)

@app.route('/video/<path:filename>')
def stream_video(filename):
    file_path = os.path.join(VIDEO_DIR, filename)
    if not os.path.isfile(file_path):
        abort(404)

    range_header = request.headers.get('Range', None)
    if not range_header:
        return send_file(file_path, mimetype='video/mp4')

    # Handle partial content (byte-range requests)
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
    app.run(debug=True)
