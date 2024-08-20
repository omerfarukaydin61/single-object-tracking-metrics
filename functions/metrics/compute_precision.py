import numpy as np

def compute_precision(ground_truth_boxes, predicted_boxes, threshold=20):
    distances = []
    for gt_box, pred_box in zip(ground_truth_boxes, predicted_boxes):
        gt_center = [(gt_box[0] + gt_box[2]) / 2, (gt_box[1] + gt_box[3]) / 2]
        pred_center = [(pred_box[0] + pred_box[2]) / 2, (pred_box[1] + pred_box[3]) / 2]
        distance = np.linalg.norm(np.array(gt_center) - np.array(pred_center))
        distances.append(distance)
    
    precision = np.sum(np.array(distances) < threshold) / len(distances)
    return precision
