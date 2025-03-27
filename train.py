from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolo11n.pt")
    model.train(
        data="cfg/dataset/VOC.yaml",
        imgsz=640,
        batch=32,
        device="0",
        workers=20,
        custom_args_dict={
            "amp": True,
            "workers": 20,
        },
        val=False
    )