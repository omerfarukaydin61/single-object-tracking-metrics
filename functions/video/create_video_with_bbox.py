import cv2
import os
from tqdm import tqdm
from typing_extensions import Literal

def create_video_with_bbox(image_folder, output_video, bbox_file, fps, add_bbox=True, format: Literal["COCO", "PascalVOC"] = "COCO"):
    if add_bbox:
        with open(bbox_file, 'r') as file:
            bbox_data = [line.strip().split(',') for line in file.readlines()]

    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    for i, image in tqdm(enumerate(images), total=len(images), desc="Processing Images"):
        frame = cv2.imread(os.path.join(image_folder, image))
        
        if add_bbox:
            bbox = bbox_data[i]
            if format == "COCO":
                x_min, y_min, bbox_width, bbox_height = [int(coord) for coord in bbox]
                x_max = x_min + bbox_width
                y_max = y_min + bbox_height
            elif format == "PascalVOC":
                x_min, y_min, x_max, y_max = [int(coord) for coord in bbox]

            cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 1)

        video.write(frame)

    cv2.destroyAllWindows()
    video.release()
