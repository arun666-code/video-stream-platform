import axios from 'axios';

const API_URL = 'http://localhost:5000/api/videos';

export const fetchVideos = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    } catch (error) {
        console.error('Error fetching videos:', error);
        throw error;
    }
};

export const fetchVideoStream = async (videoId) => {
    try {
        const response = await axios.get(`${API_URL}/${videoId}/stream`, {
            responseType: 'blob',
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching video stream:', error);
        throw error;
    }
};