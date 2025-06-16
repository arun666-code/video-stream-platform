# VStream Server

This directory contains the backend server for the VStream application. It is built with [Flask](https://flask.palletsprojects.com/).

## Features

<<<<<<< codex/run-client-code-on-windows
- List available MP4 videos from `static/videos` via `/api/videos`.
- Stream MP4 files with range request support via `/video/<filename>`.
- Optional HLS streaming using `hls_app.py` for pre-generated playlists in `static/hls`.
=======
- Upload MP4 videos via `/upload`.
- List available videos via `/api/videos`.
- Stream MP4 files with range request support via `/video/<filename>`.
- Optional HLS conversion using `hls_app.py`.
>>>>>>> main
- Serves the client application from the `client` directory.

## Setup

1. (Optional) Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place your MP4 files in `static/videos`.
4. Run the server:
   ```bash
   python app.py
   ```

<<<<<<< codex/run-client-code-on-windows
### HLS Streaming

`hls_app.py` serves pre-generated HTTP Live Streaming (HLS) playlists from `static/hls`.
Run it instead of `app.py` if you want to serve HLS content:
=======
Uploaded videos are stored in `static/videos` and metadata is stored in `videos.db`.

### HLS Streaming

`hls_app.py` includes a simple example that converts uploaded videos to
HTTP Live Streaming (HLS) format using `ffmpeg`. Run it instead of
`app.py` if you want to experiment with HLS playlists:
>>>>>>> main

```bash
python hls_app.py
```

Generated playlists and segments are saved under `static/hls`.
