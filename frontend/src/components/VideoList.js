import React, { useEffect, useState } from 'react';
import { fetchVideos } from '../services/api';
import { Link } from 'react-router-dom';

const VideoList = () => {
    const [videos, setVideos] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadVideos = async () => {
            try {
                const videoData = await fetchVideos();
                setVideos(videoData);
            } catch (error) {
                console.error("Error fetching videos:", error);
            } finally {
                setLoading(false);
            }
        };

        loadVideos();
    }, []);

    if (loading) {
        return <div>Loading videos...</div>;
    }

    return (
        <div>
            <h1>Video List</h1>
            <ul>
                {videos.map(video => (
                    <li key={video._id}>
                        <Link to={`/videos/${video._id}`}>{video.title}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default VideoList;