# Video on Demand Service

This project is a Video on Demand service that allows users to watch videos streamed from a backend server. The application is divided into two main parts: the backend and the frontend.

## Project Structure

```
video-on-demand-service
├── backend
│   ├── src
│   │   ├── server.js          # Entry point for the backend application
│   │   ├── controllers         # Contains controllers for handling requests
│   │   │   └── videoController.js # Controller for video-related requests
│   │   ├── routes              # Contains route definitions
│   │   │   └── videoRoutes.js  # Routes for video-related endpoints
│   │   └── models              # Contains Mongoose models
│   │       └── videoModel.js   # Mongoose model for video documents
│   ├── package.json            # NPM configuration for the backend
│   └── README.md               # Documentation for the backend
├── frontend
│   ├── public
│   │   └── index.html          # Main HTML file for the frontend
│   ├── src
│   │   ├── App.js              # Main component of the React application
│   │   ├── components           # Contains React components
│   │   │   ├── VideoPlayer.js   # Component for video playback
│   │   │   └── VideoList.js     # Component for displaying video list
│   │   └── services            # Contains API service functions
│   │       └── api.js          # Functions for making API calls to the backend
│   ├── package.json            # NPM configuration for the frontend
│   └── README.md               # Documentation for the frontend
└── README.md                   # Overall documentation for the project
```

## Getting Started

### Prerequisites

- Node.js (version 14 or higher)
- MongoDB (for database)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd video-on-demand-service
   ```

2. Install backend dependencies:
   ```
   cd backend
   npm install
   ```

3. Install frontend dependencies:
   ```
   cd frontend
   npm install
   ```

### Running the Application

1. Start the backend server:
   ```
   cd backend
   npm start
   ```

2. Start the frontend application:
   ```
   cd frontend
   npm start
   ```

### API Endpoints

- `GET /api/videos` - Fetch all videos
- `GET /api/videos/:id/stream` - Stream a specific video

## Usage

Once both the backend and frontend are running, navigate to `http://localhost:3000` in your web browser to access the application. You will be able to view a list of available videos and stream them directly from the server.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to add.

## License

This project is licensed under the MIT License.