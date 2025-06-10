async function fetchVideos() {
    const res = await fetch('/api/videos');
    const videos = await res.json();
    const list = document.getElementById('videoList');
    list.innerHTML = '';
    videos.forEach(v => {
        const li = document.createElement('li');
        const title = document.createElement('p');
        title.textContent = v.filename;
        const video = document.createElement('video');
        video.controls = true;
        const source = document.createElement('source');
        source.src = `/video/${v.filename}`;
        source.type = 'video/mp4';
        video.appendChild(source);
        li.appendChild(title);
        li.appendChild(video);
        list.appendChild(li);
    });
}

document.getElementById('uploadForm').addEventListener('submit', async e => {
    e.preventDefault();
    const fileInput = document.getElementById('videoFile');
    if (!fileInput.files.length) return;
    const formData = new FormData();
    formData.append('video', fileInput.files[0]);
    await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    fileInput.value = '';
    fetchVideos();
});

fetchVideos();
