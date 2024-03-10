import React, { useState, useEffect } from 'react';


export default function MusicStaff() {
    const [noteData, setNoteData] = useState(null); // State to store fetched note data
    const [isPlaying, setIsPlaying] = useState(false); // State to track audio playback
  
    useEffect(() => {
      const fetchNoteData = async () => {
        const response = await fetch('172.16.176.46'); // Replace with your API URL
        const data = await response.json();
        setNoteData(data);
      };
  
      fetchNoteData();
    }, []); // Run useEffect only on component mount
  
    const handlePlayPause = () => {
      if (isPlaying) {
        // Stop audio playback (implementation depends on note data format)
        setIsPlaying(false);
      } else {
        // Start audio playback (implementation depends on note data format)
        setIsPlaying(true);
      }
    };

          return (
            <div className="flex flex-col items-center gap-2">
              {noteData ? (
                <div>
                  <h2>{noteData.title}</h2>
                  <p>{noteData.frequency}</p>
                  {noteData.audio && (
                    <button onClick={handlePlayPause}>{isPlaying ? 'Pause' : 'Play'}</button>
                  )}
                </div>
              ) : (
                <p>Loading note...</p>
              )}
            </div>
          );
}