# VStream Server

This directory contains the backend server for the VStream application. It is built with [Flask](https://flask.palletsprojects.com/).

## Features

- List available MP4 videos from `static/videos` via `/api/videos`.
- Stream MP4 files with range request support via `/video/<filename>`.
- Optional HLS streaming using `hls_app.py` for pre-generated playlists in `static/hls`.
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

### HLS Streaming

`hls_app.py` serves pre-generated HTTP Live Streaming (HLS) playlists from `static/hls`.
Run it instead of `app.py` if you want to serve HLS content:

```bash
python hls_app.py
```

Generated playlists and segments are saved under `static/hls`.
