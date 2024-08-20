def compute_iou(boxA, boxB):
    # Determine the coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # Compute the area of intersection
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # Compute the area of both the prediction and ground-truth rectangles
    boxAArea = max(0, boxA[2] - boxA[0] + 1) * max(0, boxA[3] - boxA[1] + 1)
    boxBArea = max(0, boxB[2] - boxB[0] + 1) * max(0, boxB[3] - boxB[1] + 1)

    # Prevent division by zero by checking if the area is zero
    if boxAArea == 0 or boxBArea == 0:
        return 0.0  # Return 0 IoU if either box has zero area

    # Compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the intersection area
    iou = interArea / float(boxAArea + boxBArea - interArea)

    return iou
