import argparse
import json
import os
from pathlib import Path
from ultralytics import YOLO

def run_inference(weights, input_folder, output_folder, log_folder, conf=0.5):
    model = YOLO(weights)

    os.makedirs(output_folder, exist_ok=True)
    os.makedirs(log_folder, exist_ok=True)

    # Loop through images
    for img_file in Path(input_folder).glob("*.jpg"):
        results = model(img_file, conf=conf, imgsz=640, save=True, project=output_folder, name="")

        detections_list = []
        for r in results:
            for box in r.boxes:
                label = model.names[int(box.cls[0])]
                confidence = float(box.conf[0])
                x1, y1, x2, y2 = map(float, box.xyxy[0])

                detections_list.append({
                    "label": label,
                    "confidence": confidence,
                    "bbox": [x1, y1, x2, y2]
                })
                print(f"[{img_file.name}] {label} detected with confidence {confidence:.2f}")

        log_data = {
            "filename": img_file.name,
            "detections": detections_list
        }

        with open(os.path.join(log_folder, img_file.stem + ".json"), "w") as f:
            json.dump(log_data, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--weights", type=str, required=True, help="Path to trained model (best.pt)")
    parser.add_argument("--input", type=str, required=True, help="Input folder of images")
    parser.add_argument("--output", type=str, required=True, help="Output folder for annotated images")
    parser.add_argument("--logs", type=str, required=True, help="Folder for JSON logs")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold")
    args = parser.parse_args()

    run_inference(args.weights, args.input, args.output, args.logs, args.conf)
