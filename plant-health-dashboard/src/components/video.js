import React from 'react';

const LiveVideo = () => {
    return (
        <div className="live-video-container">
            {/* <img src="/video_feed" alt="Live Video Feed" /> */}
            <img src="http://localhost:5000/api/video_feed" alt="Live Video Feed" />
        </div>
    );
}

export default LiveVideo;
