#!/bin/bash

if [ $# -eq 0 ]; then
    echo "No URL provided. Usage: $0 <video_url>"
    exit 1
fi

VIDEO_URL=$1

yt-dlp -f bestaudio --extract-audio --audio-format mp3 "$VIDEO_URL"

if [ $? -eq 0 ]; then
    echo "Audio downloaded successfully in MP3 format."
else
    echo "Failed to download audio. Please check the URL or your internet connection."
fi
