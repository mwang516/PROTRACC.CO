import cv2
import mediapipe as mp
import json
import os
import numpy as np

def mediaToPose(path):
    print("Starting mediaToPose function")
    absolute_path = os.path.abspath(path)
    print(f"Attempting to open video at: {absolute_path}")
    
    # Try to check if file exists
    if os.path.exists(absolute_path):
        print(f"File exists at {absolute_path}")
    else:
        print(f"File does not exist at {absolute_path}")
    
    # Initialize MediaPipe pose and drawing modules
    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils
    
    # Try to open video
    cap = cv2.VideoCapture(absolute_path)
    if cap.isOpened():
        print("Successfully opened video file")
    else:
        print("Failed to open video file")

    def process_frame(frame, pose):
        """Convert frame to RGB, process it, and return pose landmarks."""
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_rgb = cv2.GaussianBlur(img_rgb, (5, 5), 0)
        return pose.process(img_rgb)

    def draw_landmarks(image, results):
        """Draw pose landmarks on an image or frame."""
        if results.pose_landmarks:
            mp_draw.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    def save_landmarks_json(results, output_path):
        """Extract and save pose landmarks to a JSON file."""
        if results.pose_world_landmarks:
            pose_landmarks_list = []
            for id, lm in enumerate(results.pose_world_landmarks.landmark):
                landmarks = {
                    'id': id,
                    'x': lm.x,
                    'y': lm.y,
                    'z': lm.z,
                    'visibility': lm.visibility
                }
                pose_landmarks_list.append(landmarks)
            
            with open(output_path, 'w') as json_file:
                json.dump(pose_landmarks_list, json_file, indent=4)
            print(f"Pose landmarks data saved to {output_path}")

    def save_cameramarks_json(results, output_path):
        """Extract and save pose landmarks to a JSON file."""
        if results.pose_landmarks:
            pose_phone_landmarks_list = []
            for id, lm in enumerate(results.pose_landmarks.landmark):
                landmarks = {
                    'id': id,
                    'x': lm.x,
                    'y': lm.y,
                    'z': lm.z,
                    'visibility': lm.visibility
                }
                pose_phone_landmarks_list.append(landmarks)
            
            with open(output_path, 'w') as json_file:
                json.dump(pose_phone_landmarks_list, json_file, indent=4)
            print(f"Pose landmarks data saved to {output_path}")

    def process_image(image_path, output_json_phone=None, output_json_real=None):
        """Process a single image for pose detection and optionally save the result as JSON."""
        image = cv2.imread(image_path)
        pose = mp_pose.Pose(static_image_mode=True, model_complexity=1, min_detection_confidence=0.5)
        results = process_frame(image, pose)
        
        draw_landmarks(image, results)
        if output_json_real:
            save_cameramarks_json(results, output_json_phone)
            save_landmarks_json(results, output_json_real)
        
        cv2.imshow("Pose Detection", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def process_video(video_path,output_json_phone=None, output_json_real=None, output_video=None):
        """Process a video for pose detection and optionally save the result as JSON and/or video."""
        cap = cv2.VideoCapture(video_path)
        pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
        
        if output_video:
            fps = cap.get(cv2.CAP_PROP_FPS)
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))
        
        pose_landmarks_real = []
        pose_landmarks_phone= []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = process_frame(frame, pose)
            draw_landmarks(frame, results)
            scale = 40
            landmarks_world = {}
            if results.pose_world_landmarks:
                for id, lm in enumerate(results.pose_world_landmarks.landmark):
                    landmarks_world[id] = {
                        'x': lm.x * scale,
                        'y': lm.y * scale,
                        'z': lm.z * scale,
                        'visibility': lm.visibility
                    }
                pose_landmarks_real.append(landmarks_world)

            landmarks_phone = {}
            if results.pose_landmarks:
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    landmarks_phone[id] = {
                        'x': (lm.x - 0.5) * scale, # minus 0.5 to centre
                        'y': lm.y * scale,
                        'z': (lm.z) * scale,
                        'visibility': lm.visibility
                    }
                pose_landmarks_phone.append(landmarks_phone)
            
            if output_video:
                out.write(frame)

            cv2.imshow("Pose Detection", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        if output_json_real:
            with open(output_json_real, 'w') as json_file:
                json.dump(pose_landmarks_real, json_file, indent=4)
            print(f"Pose landmarks data saved to {output_json_real}")
        if output_json_phone:
            with open(output_json_phone, 'w') as json_file:
                json.dump(pose_landmarks_phone, json_file, indent=4)
            print(f"Pose landmarks data saved to {output_json_phone}")
        
        cap.release()
        if output_video:
            out.release()
        cv2.destroyAllWindows()

    # Example usage:
    # process_image('image.jpeg', 'image_pose.json')

    def load_data(file_path):
        """Load pose landmarks data from a JSON file."""
        with open(file_path, 'r') as f:
            return json.load(f)

    def calculate_midpoint(point1, point2):
        """Calculate the midpoint between two points."""
        return {
            'x': (point1['x'] + point2['x']) / 2,
            'y': (point1['y'] + point2['y']) / 2,
            'z': point2['z'] # not really midpoint
        }

    def generate_midpoints(data, joint_ids):
        """Generate midpoints for the specified joint IDs."""
        midpoints = []
        for frame in data:
            left_hip = frame[joint_ids['left_hip']]
            right_hip = frame[joint_ids['right_hip']]
            midpoint = calculate_midpoint(left_hip, right_hip)
            midpoints.append(midpoint)
        return midpoints

    def save_midpoints(midpoints, output_path):
        """Save the calculated midpoints to a JSON file."""
        with open(output_path, 'w') as json_file:
            json.dump(midpoints, json_file, indent=4)
        print(f"Midpoints data saved to {output_path}")

    process_video(path,output_json_phone="server/data/phone_landmarks.json", output_json_real="server/data/pose_landmarks.json")

    # Load the data
    input_file = 'server/data/phone_landmarks.json'
    output_file = 'server/data/midpoints.json'
    joint_ids = {'left_hip': "23", 'right_hip': "24"}

    data = load_data(input_file)

    # Generate midpoints for the hips
    midpoints = generate_midpoints(data, joint_ids)

    # Save the midpoints to a JSON file
    save_midpoints(midpoints, output_file)

    with open('server/data/pose_landmarks.json') as f:
        real = json.load(f)

    with open('server/data/midpoints.json') as f:
        midpoints = json.load(f)

    # Iterate through frames and joints, updating the x-coordinate

    for index, frame in enumerate(real):
        for joint_id, joint_data in frame.items():
            joint_id = int(joint_id)  # Convert joint ID to an integer
            joint_data["x"] += (midpoints[index]['x']) * 5.4
            joint_data["z"] += (midpoints[index]['z']) * 5.4
            joint_data["y"] += (midpoints[index]['y']) * 5.4

    max_y = max(max(frame["32"]['y'] for frame in real), max(frame["31"]['y'] for frame in real))

    for index, frame in enumerate(real):
        for joint_id, joint_data in frame.items():
            joint_id = int(joint_id)  # Convert joint ID to an integer
            joint_data["y"] -= max_y

    with open('/Users/matthewwang/Desktop/nwHacks 2025/posture-visioner/public/moved.json', 'w') as f:
        json.dump(real, f, indent=4)

mediaToPose("/Users/matthewwang/Desktop/nwHacks 2025/posture-visioner/server/videos/downloaded_video.mp4")