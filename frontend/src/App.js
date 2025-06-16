import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import VideoList from './components/VideoList';
import VideoPlayer from './components/VideoPlayer';

function App() {
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        const fetchVideos = async () => {
            const response = await fetch('/api/videos');
            const data = await response.json();
            setVideos(data);
        };

        fetchVideos();
    }, []);

    return (
        <Router>
            <div className="App">
                <h1>Video On Demand Service</h1>
                <Switch>
                    <Route path="/" exact>
                        <VideoList videos={videos} />
                    </Route>
                    <Route path="/video/:id" component={VideoPlayer} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;