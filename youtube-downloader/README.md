# YouTube Downloader

A simple web app for downloading YouTube videos in 4K or audio in MP3 format.

## Features
- Download YouTube videos in 4K resolution.
- Extract and download MP3 audio from YouTube videos.

## Get started
- eval "$(ssh-agent -s)"
- ssh-add /c/Users/Administrator/.ssh/github_key
- if you don't have python installed, install it and add it to the Path like this:
  Add Python to the System PATH
C:\Users\Administrator\AppData\Local\Programs\Python\Python313

Add to PATH:

    Open the Start menu and search for "Environment Variables."
    Click on "Edit the system environment variables."
    In the System Properties window, click on the Environment Variables button.
    In the Environment Variables window:
        Under "System variables," scroll down to find the variable named Path and select it.
        Click "Edit."
        Add a new entry for Python's directory:

C:\Users\Administrator\AppData\Local\Programs\Python\Python313

Also, add Python's Scripts directory:

    C:\Users\Administrator\AppData\Local\Programs\Python\Python313\Scripts

Click OK to close all dialogs.
Restart the IDE.

- export PATH=$PATH:/c/Users/Administrator/AppData/Local/Programs/Python/Python313/Scripts
- python backend/app.py
