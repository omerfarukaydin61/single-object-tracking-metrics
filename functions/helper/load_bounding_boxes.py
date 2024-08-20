def load_bounding_boxes(file_path):
    with open(file_path, 'r') as file:
        boxes = [list(map(int, line.strip().split(','))) for line in file]
    return boxes
