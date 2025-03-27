from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("runs/detect/train4/weights/best.pt")
    model.val(
        data="cfg/dataset/VOC.yaml",
        imgsz=640,
        batch=32,
        device="0",
        workers=20,
        save_json=True,
    )
