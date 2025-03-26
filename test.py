from ultralytics import YOLO

model = YOLO("yolo11n.pt")


model.val(
    data="cfg/dataset/VOC.yaml",
    imgsz=640,
    batch=32,
    device="0",
    workers=20,
)
