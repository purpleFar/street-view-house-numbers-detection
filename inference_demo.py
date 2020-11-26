# -*- coding: utf-8 -*-
import os
import json
from mmdet.apis import init_detector, inference_detector

# Specify the path to model config and checkpoint file
config_file = "configs/faster_rcnn/faster_rcnn_r34_fpn_1x_coco.py"
checkpoint_file = "work_dirs/faster_rcnn_r34_fpn_1x_coco/latest.pth"
imgDir = "test"
result_list = []

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device="cuda:0")

# test a single image and show the results
for img_num in range(1, 13069):
    img = os.path.join("test", str(img_num) + ".png")
    print(img)
    result = inference_detector(model, img)
    tmp_dict = {"bbox": [], "score": [], "label": [], "img": 0}
    for i, aClass in enumerate(result):
        for box in aClass:
            box = box.tolist()
            if box[-1] >= 0.5:
                tmp_dict["bbox"].append([box[1], box[0], box[3], box[2]])
                tmp_dict["score"].append(box[-1])
                tmp_dict["label"].append(i + 1)
    tmp_dict["img"] = img_num
    result_list.append(tmp_dict)
with open("0856735_13.json", "w", encoding="utf-8") as f:
    json.dump(result_list, f, ensure_ascii=False)
