// import React from 'react';

// const LiveVideo = () => {
//     return (
//         <div className="live-video-container">
//             {/* <img src="/video_feed" alt="Live Video Feed" /> */}
//             <img src="http://localhost:5000/api/video_feed" alt="Live Video Feed" />
//         </div>
//     );
// }

// export default LiveVideo;
import React from 'react';
import { Card, CardContent } from '@material-ui/core';

const LiveVideo = () => {
    return (
        <Card style={{ height: '400px' }}>
            <CardContent style={{ height: '100%', padding: 0 }}>
                <div className="live-video-container" style={{ height: '100%' }}>
                    <img src="http://localhost:5000/api/video_feed" alt="Live Video Feed" style={{ height: '100%', width: '100%', objectFit: 'cover' }} />
                </div>
            </CardContent>
        </Card>
    );
}

export default LiveVideo;
