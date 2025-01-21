import sys
import site

# Add Python 3.11 site-packages to path
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages')

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from pymongo import MongoClient
import gridfs
import os
from dotenv import load_dotenv
from bson import ObjectId
from werkzeug.utils import secure_filename
import subprocess

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './server/videos'
CORS(app)

MONGODB_URI = os.getenv("MONGODB_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGODB_URI)
db = client['myDatabase'] 
fs = gridfs.GridFS(db, collection='Videos')

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)  # Create the directory if it doesn't exist

@app.route('/upload', methods=['POST'])
def video_upload():
    if 'video' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Store the video in GridFS
    file_id = fs.put(file, filename=file.filename)

    return jsonify({'message': 'Video uploaded successfully', 'file_id': str(file_id)}), 200

@app.route('/get_video', methods=['GET'])
def get_video():
    print("get_video endpoint hit")
    file_id = request.args.get('file_id')
    print(f"Requested file_id: {file_id}")
    if not file_id:
        return jsonify({'error': 'No file_id provided'}), 400

    try:
        # Convert the string file_id to ObjectId
        video = fs.get(ObjectId(file_id))
        return send_file(video, mimetype='video/mp4')
    except gridfs.errors.NoFile:
        return jsonify({'error': 'Video not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['video']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    print(f"File saved to {os.path.join(app.config['UPLOAD_FOLDER'], filename)}")

    # Explicitly use python3.11 for the subprocess
    subprocess.run(['/usr/local/bin/python3.11', 'server/mediaToPose.py'])
    
    return jsonify({'message': 'Video saved successfully', 'filename': filename}), 200

if __name__ == '__main__':
    app.run(debug=True)