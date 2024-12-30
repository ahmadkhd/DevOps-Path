#!/bin/bash

if [ $# -eq 0 ]; then
    echo "No URL provided. Usage: $0 <video_url>"
    exit 1
fi

VIDEO_URL=$1

yt-dlp -f "bestvideo[height<=2160]+bestaudio/best[height<=2160]" --merge-output-format mp4 "$VIDEO_URL"

if [ $? -eq 0 ]; then
    echo "Video downloaded successfully in 4K (if available)."
else
    echo "Failed to download video. Please check the URL or your internet connection."
fi
