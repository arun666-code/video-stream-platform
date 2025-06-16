# VStream Server

This directory contains the backend server for the VStream application. It is built with [Flask](https://flask.palletsprojects.com/).

## Features

- Upload MP4 videos via `/upload`.
- List available videos via `/api/videos`.
- Stream MP4 files with range request support via `/video/<filename>`.
- Optional HLS conversion using `hls_app.py`.
- Serves the client application from the `client` directory.

## Setup

1. (Optional) Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python app.py
   ```

Uploaded videos are stored in `static/videos` and metadata is stored in `videos.db`.

### HLS Streaming

`hls_app.py` includes a simple example that converts uploaded videos to
HTTP Live Streaming (HLS) format using `ffmpeg`. Run it instead of
`app.py` if you want to experiment with HLS playlists:

```bash
python hls_app.py
```

Generated playlists and segments are saved under `static/hls`.
