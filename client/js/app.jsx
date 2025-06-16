const { useState, useEffect } = React;

function App() {
    const [videos, setVideos] = useState([]);
    const [file, setFile] = useState(null);

    const fetchVideos = async () => {
        const res = await fetch('/api/videos');
        const data = await res.json();
        setVideos(data);
    };

    useEffect(() => {
        fetchVideos();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;
        const formData = new FormData();
        formData.append('video', file);
        await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        setFile(null);
        document.getElementById('fileInput').value = '';
        fetchVideos();
    };

    return (
        <div className="container">
            <h1>VStream</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="file"
                    accept="video/mp4"
                    id="fileInput"
                    onChange={(e) => setFile(e.target.files[0])}
                    required
                />
                <button type="submit">Upload</button>
            </form>
            <h2>Videos</h2>
            <ul>
                {videos.map((v) => (
                    <li key={v.id}>
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
