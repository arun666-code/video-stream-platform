# VStream

A minimal web-based video streaming application built with [Flask](https://flask.palletsprojects.com/).

## Features

- Lists all `.mp4` files found in `static/videos`.
- Streams video files with support for range requests (allowing users to seek within the video).

## Setup

1. (Optional) Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place your `.mp4` files into the `static/videos` directory.

## Running

```bash
python app.py
```

The application will be available at `http://localhost:5000/`.

## Notes

This project provides a very basic demonstration of a video streaming application. It does not implement authentication, transcoding, or advanced features found in commercial streaming services.
