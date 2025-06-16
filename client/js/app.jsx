const { useState, useEffect } = React;

function App() {
    const [videos, setVideos] = useState([]);

    const fetchVideos = async () => {
        const res = await fetch('/api/videos');
        const data = await res.json();
        setVideos(data);
    };

    useEffect(() => {
        fetchVideos();
    }, []);

    const handleRefresh = () => {
        fetchVideos();
    };

    return (
        <div className="container">
            <h1>VStream</h1>
            <div className="controls">
                <button onClick={handleRefresh}>Refresh List</button>
            </div>
            <h2>Videos</h2>
            <ul className="video-list">
                {videos.map((v) => (
                    <li key={v.id} className="video-card">
                        <p>{v.filename}</p>
                        <video controls>
                            <source src={`/video/${v.filename}`} type="video/mp4" />
                        </video>
                    </li>
                ))}
            </ul>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
