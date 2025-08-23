# Gloved vs Ungloved Hand Detection

This folder contains:

- `detection_script.py` — Inference script that reads a folder of images and outputs annotated images + per-image JSON logs.
- `output_folder/` — Sample annotated images (add 3–5 images after you run the script).
- `detections_logs/` — Per-image JSON logs in the required schema generted by the script.
- `models/` - folder containing YOLOv8 weights.
- `input_folder/` - folder conatining images to be processed.

---

## 📂 Project Structure
```
CVPipeline/
│── detection_script.py     # Main inference script
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
│── models/                 # Place your trained YOLO weights (best.pt)
│── input_folder/           # Folder containing input images
│── output_folder/          # Annotated images will be saved here
│── detections_logs/        # JSON logs for detections will be saved here
```

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Vision_Pipeline.git
   cd Vision_Pipeline
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running Inference
Run the script with:

```bash
python detection_script.py \
  --weights models/best.pt \
  --input input_folder \
  --output output_folder \
  --logs detections_logs \
  --conf 0.25
```

### Arguments:
- `--weights` → Path to YOLOv8 weights (`best.pt`)  
- `--input` → Folder containing input images  
- `--output` → Folder where annotated images will be saved  
- `--logs` → Folder where JSON detection logs will be stored  
- `--conf` → Confidence threshold (default: 0.25, recommend: 0.25–0.5)  

---

## 📝 Output
1. **Annotated images** → saved in `output_folder`  
2. **JSON logs** → one per image, stored in `detections_logs/`  

### Example JSON log:
```json
{
  "filename": "image1.jpg",
  "detections": [
    {
      "label": "Hand in glove detection",
      "confidence": 0.87,
      "bbox": [100.5, 200.3, 250.8, 400.6]
    }
  ]
}
```
If  bare hand is detected:
```json
{
  "filename": "image2.jpg",
  "detections": [
    {
      "label": "Hand",
      "confidence": 0.0,
      "bbox": []
    }
  ]
}
```
## 📊 Example Terminal Output
```
[image1.jpg] glove detected with confidence 0.87
[image2.jpg] hand detected with confidence 0.42
[image3.jpg] No detection → assuming no detection in the image
```
