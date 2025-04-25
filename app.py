from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Add a static folder configuration for videos
VIDEO_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'videos')
os.makedirs(VIDEO_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sankey')
def sankey():
    # This route will display your embedded Sankey diagram
    return render_template('sankey.html')

@app.route('/video')
def video():
    # Get list of videos in the video folder
    video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith('.mp4')]
    return render_template('video.html', video_files=video_files)

@app.route('/static/videos/<filename>')
def serve_video(filename):
    return send_from_directory(VIDEO_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)