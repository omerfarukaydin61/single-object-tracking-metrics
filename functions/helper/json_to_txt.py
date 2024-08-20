import json
import os 

def json_parse(json_file):
    # Split the file name to determine the type (vis or sot)
    filename = os.path.basename(json_file)
    parts = filename.split('-')

    txt_file_path = json_file.replace("log", 'txt').replace('.json', '.txt')

    name = f"{parts[10]}-{parts[1]}-{parts[2]}-{parts[3]}"
    device_name = parts[9]
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Extract video details from the JSON data
    video_duration = data.get("video_duration", 0)
    video_fps = data.get("video_fps", 0)
    total_process_time = data.get("total_process_time", 0)
    total_frames = data.get("total_frames", 0)

    # Open a text file to save the extracted coordinates
    with open(txt_file_path, 'w') as txt_file:
        for i, frame in enumerate(data['tracking_results']):
            bbox = frame['track_bboxes']
            if "vis" in parts:
                # If it's a vis JSON, extract class and score along with bbox
                class_id, x1, y1, x2, y2, score = bbox[0], bbox[1], bbox[2], bbox[3], bbox[4], bbox[5]
                txt_file.write(f"{int(x1)},{int(y1)},{int(x2)},{int(y2)}\n")
            elif "sot" or "default_tracker" in parts:
                # If it's a sot JSON, only extract bbox coordinates
                x1, y1, x2, y2 = bbox[0], bbox[1], bbox[2], bbox[3]
                
                txt_file.write(f"{int(x1)},{int(y1)},{int(x2)},{int(y2)}\n")
            else:
                raise ValueError("Invalid JSON file name. Must contain 'vis' or 'sot'.")

    # Return the path to the txt file, the extracted video duration, fps, total process time, and total frames
    return name, txt_file_path, video_duration, video_fps, total_process_time, total_frames, device_name
