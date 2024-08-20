from functions.helper.load_bounding_boxes import load_bounding_boxes
from functions.metrics.average_iou import average_iou
from functions.metrics.compute_precision import compute_precision
from functions.metrics.success_rate import success_rate
from functions.metrics.compute_fps import compute_fps
from functions.helper.json_to_txt import json_parse
import pandas as pd
import yaml

config = yaml.safe_load(open(r'configs/config.yaml', 'r'))

name, predicted_boxes_txt, video_duration, video_fps, total_process_time, total_frames, device_name = json_parse(config['log_json_file'])

# Load ground truth and predicted bounding boxes
ground_truth_boxes = load_bounding_boxes(config['ground_truth_file'])
predicted_boxes = load_bounding_boxes(predicted_boxes_txt)

# Calculate metrics
avg_iou = average_iou(ground_truth_boxes, predicted_boxes)
precision = compute_precision(ground_truth_boxes, predicted_boxes)
success_rate_val = success_rate(ground_truth_boxes, predicted_boxes, iou_threshold=config['iou_threshold'])

process_fps = compute_fps(total_process_time, total_frames)

print("Device Name: ", device_name)
# Print results
print(f"Results for {name}")
print(f"Average IoU: {avg_iou:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Success Rate: {success_rate_val:.4f}")

print(f"Video Duration: {video_duration:.2f}")
print(f"Video FPS: {video_fps:.2f}")
print(f"Total Process Time: {total_process_time:.2f}")
print(f"Total Frames: {total_frames}")
print(f"Process FPS: {process_fps:.2f}")

# Load existing results
df = pd.read_csv('results.csv')

# Check if the video name already exists in the DataFrame
if name not in df['Name'].values:
    # Create a new DataFrame with the new results
    new_row = pd.DataFrame([{
        'Name': name,
        'Average IoU': avg_iou,
        'Precision': precision,
        'Success Rate': success_rate_val,
        'Video Duration': video_duration,
        'Video FPS': video_fps,
        'Total Process Time': total_process_time,
        'Total Frames': total_frames,
        'Process FPS': process_fps,
        'Device': device_name
    }])

    # Concatenate the new row to the existing DataFrame
    df = pd.concat([df, new_row], ignore_index=True)

# Save the updated DataFrame back to the CSV file
df.to_csv(config['result_csv_file'], index=False)