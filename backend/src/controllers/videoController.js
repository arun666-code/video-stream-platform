class VideoController {
    constructor(videoModel) {
        this.videoModel = videoModel;
    }

    async getAllVideos(req, res) {
        try {
            const videos = await this.videoModel.find({});
            res.status(200).json(videos);
        } catch (error) {
            res.status(500).json({ message: 'Error fetching videos', error });
        }
    }

    async streamVideo(req, res) {
        const videoId = req.params.id;
        try {
            const video = await this.videoModel.findById(videoId);
            if (!video) {
                return res.status(404).json({ message: 'Video not found' });
            }

            const videoPath = video.videoUrl; // Assuming videoUrl is a path to the video file
            const stat = fs.statSync(videoPath);
            const fileSize = stat.size;
            const range = req.headers.range;

            if (range) {
                const parts = range.replace(/bytes=/, "").split("-");
                const start = parseInt(parts[0], 10);
                const end = parts[1] ? parseInt(parts[1], 10) : fileSize - 1;

                res.writeHead(206, {
                    "Content-Range": `bytes ${start}-${end}/${fileSize}`,
                    "Accept-Ranges": "bytes",
                    "Content-Length": end - start + 1,
                    "Content-Type": "video/mp4",
                });

                const stream = fs.createReadStream(videoPath, { start, end });
                stream.pipe(res);
            } else {
                res.writeHead(200, {
                    "Content-Length": fileSize,
                    "Content-Type": "video/mp4",
                });
                fs.createReadStream(videoPath).pipe(res);
            }
        } catch (error) {
            res.status(500).json({ message: 'Error streaming video', error });
        }
    }
}

module.exports = VideoController;