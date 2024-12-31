from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

# Route to serve the frontend (index.html)
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')  # Adjust the path as needed

# Static file route for CSS, JS, etc.
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory('../frontend', path)


@app.route('/download/video', methods=['GET'])
def download_video():
    url = request.args.get('url')
    if not url:
        return jsonify({"success": False, "message": "URL is required"}), 400

    try:
        # Run the Bash script for video download
        result = subprocess.run(
            ["./youtube_downloader_video.sh", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            return jsonify({"success": True, "message": result.stdout.decode("utf-8")})
        else:
            return jsonify({"success": False, "message": result.stderr.decode("utf-8")})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/download/audio', methods=['GET'])
def download_audio():
    url = request.args.get('url')
    if not url:
        return jsonify({"success": False, "message": "URL is required"}), 400

    try:
        # Run the Bash script for audio download
        result = subprocess.run(
            ["./youtube_downloader_audio.sh", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            return jsonify({"success": True, "message": result.stdout.decode("utf-8")})
        else:
            return jsonify({"success": False, "message": result.stderr.decode("utf-8")})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
