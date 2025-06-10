# VStream Server

This directory contains the backend server for the VStream application. It is built with [Flask](https://flask.palletsprojects.com/).

## Features

- Upload MP4 videos via `/upload`.
- List available videos via `/api/videos`.
- Stream videos with range request support via `/video/<filename>`.
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
