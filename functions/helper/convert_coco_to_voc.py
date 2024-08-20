bbox_file = 'person-10-trimmed\groundtruth\groundtruth.txt'
out_bbox_file = 'person-10-trimmed\groundtruth\groundtruth_pascal_voc.txt'
# Load and convert the contents of the bbox label.txt file from COCO to Pascal VOC format
def convert_coco_to_voc(input_file, output_file):
    with open(input_file, 'r') as file:
        # Read the bounding boxes assuming they are comma-separated
        coco_bboxes = [line.strip().split(',') for line in file.readlines()]
    
    voc_bboxes = []
    
    for bbox in coco_bboxes:
        # Convert each bounding box from string to float
        x, y, width, height = map(int, bbox)
        
        # Convert to Pascal VOC format
        xmin = x
        ymin = y
        xmax = x + width
        ymax = y + height
        
        # Append the converted bbox to the list
        voc_bboxes.append(f"{xmin},{ymin},{xmax},{ymax}\n")
    
    # Write the converted bboxes to the output file
    with open(output_file, 'w') as file:
        file.writelines(voc_bboxes)

convert_coco_to_voc(bbox_file, out_bbox_file)