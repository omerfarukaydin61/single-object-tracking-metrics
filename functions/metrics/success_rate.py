from .compute_iou import compute_iou

def success_rate(ground_truth_boxes, predicted_boxes, iou_threshold=0.5):
    successes = 0
    for gt_box, pred_box in zip(ground_truth_boxes, predicted_boxes):
        iou = compute_iou(gt_box, pred_box)
        if iou >= iou_threshold:
            successes += 1
    return successes / len(ground_truth_boxes)
