from flask import Flask, request, jsonify, send_file
import os
import yt_dlp

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"  # Directory to store downloaded files

# Ensure the download directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

@app.route('/download/video', methods=['GET'])
def download_video():
    url = request.args.get('url')
    if not url:
        return jsonify({'success': False, 'message': 'URL is required'}), 400

    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return jsonify({'success': True, 'downloadUrl': f'/file/{os.path.basename(filename)}'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/download/audio', methods=['GET'])
def download_audio():
    url = request.args.get('url')
    if not url:
        return jsonify({'success': False, 'message': 'URL is required'}), 400

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info).replace(".webm", ".mp3")

        return jsonify({'success': True, 'downloadUrl': f'/file/{os.path.basename(filename)}'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/file/<filename>', methods=['GET'])
def serve_file(filename):
    file_path = os.path.join(DOWNLOAD_DIR, filename)
    if not os.path.exists(file_path):
        return jsonify({'success': False, 'message': 'File not found'}), 404

    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
