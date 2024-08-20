from .compute_iou import compute_iou

def average_iou(ground_truth_boxes, predicted_boxes):
    iou_sum = 0
    for gt_box, pred_box in zip(ground_truth_boxes, predicted_boxes):
        iou_sum += compute_iou(gt_box, pred_box)
    return iou_sum / len(ground_truth_boxes)
