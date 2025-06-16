const express = require('express');
const VideoController = require('../controllers/videoController');

const router = express.Router();
const videoController = new VideoController();

function setRoutes(app) {
    router.get('/videos', videoController.getAllVideos.bind(videoController));
    router.get('/videos/:id/stream', videoController.streamVideo.bind(videoController));

    app.use('/api', router);
}

module.exports = setRoutes;