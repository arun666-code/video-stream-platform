# Video on Demand Service - Backend

## Overview
This is the backend service for the Video on Demand application. It is built using Node.js and Express, and it connects to a MongoDB database to manage video data.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd video-on-demand-service/backend
   ```

2. **Install Dependencies**
   Make sure you have Node.js installed. Then run:
   ```bash
   npm install
   ```

3. **Environment Variables**
   Create a `.env` file in the `backend` directory and add your MongoDB connection string:
   ```
   MONGODB_URI=<your_mongodb_connection_string>
   PORT=5000
   ```

4. **Start the Server**
   To start the backend server, run:
   ```bash
   npm start
   ```

## API Endpoints

### Videos

- **GET /api/videos**
  - Description: Fetch all videos.
  - Response: List of videos.

- **GET /api/videos/:id/stream**
  - Description: Stream a video by ID.
  - Response: Video stream.

## Directory Structure

- `src/`
  - `server.js`: Entry point for the application.
  - `controllers/`: Contains video-related request handlers.
  - `routes/`: Defines API routes for video endpoints.
  - `models/`: Contains Mongoose models for the database.

## Technologies Used
- Node.js
- Express
- Mongoose
- MongoDB

## License
This project is licensed under the MIT License.