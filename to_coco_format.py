# -*- coding: utf-8 -*-
import random as r
import os
from PIL import Image
import h5py
import json


train_folder = "train"
trainImgIDSet = set()
errorImgIDSet = set()
coco_dict = {
    "images": [],
    "annotations": [],
    "categories": [{"id": i, "name": "{}".format(i % 10)} for i in range(1, 11)],
}

val_coco_dict = {
    "images": [],
    "annotations": [],
    "categories": [{"id": i, "name": "{}".format(i % 10)} for i in range(1, 11)],
}

error_coco_dict = {
    "images": [],
    "annotations": [],
    "categories": [{"id": i, "name": "{}".format(i % 10)} for i in range(1, 11)],
}

for root, dirs, files in os.walk(train_folder):
    for f in files:
        name_cut = f.split(".")
        if name_cut[-1] == "png":
            im = Image.open(os.path.join(root, f))
            width, height = im.size
            temp_dict = {
                "file_name": f,
                "height": height,
                "width": width,
                "id": int(name_cut[0]),
            }
            if r.randint(0, 33402) > 1000:
                coco_dict["images"].append(temp_dict)
                trainImgIDSet.add(int(name_cut[0]))
            else:
                val_coco_dict["images"].append(temp_dict)
            if r.randint(0, 33402) < 100:
                error_coco_dict["images"].append(temp_dict)
                errorImgIDSet.add(int(name_cut[0]))


def get_name(index, hdf5_data):
    name = hdf5_data["/digitStruct/name"]
    return "".join([chr(v[0]) for v in hdf5_data[name[index][0]][()]])


def get_bbox(index, hdf5_data):
    attrs = {}
    item = hdf5_data["digitStruct"]["bbox"][index].item()
    for key in ["label", "left", "top", "width", "height"]:
        attr = hdf5_data[item][key]
        values = (
            [hdf5_data[attr[()][i].item()][()][0][0] for i in range(len(attr))]
            if len(attr) > 1
            else [attr[()][0][0]]
        )
        attrs[key] = values
    return attrs


def img_boundingbox_data_constructor(mat_file):
    f = h5py.File(mat_file, "r")
    print("image bounding box data construction starting...")
    for j in range(f["/digitStruct/bbox"].shape[0]):
        row_dict = get_bbox(j, f)
        for i in range(len(row_dict["label"])):
            temp_dict = {
                "area": row_dict["width"][i] * row_dict["height"][i],
                "iscrowd": 0,
                "image_id": int(get_name(j, f).split(".")[0]),
                "bbox": [
                    row_dict["left"][i],
                    row_dict["top"][i],
                    row_dict["width"][i],
                    row_dict["height"][i],
                ],
                "category_id": int(row_dict["label"][i]),
                "id": j,
            }
            if int(get_name(j, f).split(".")[0]) in trainImgIDSet:
                coco_dict["annotations"].append(temp_dict)
            else:
                val_coco_dict["annotations"].append(temp_dict)
            if int(get_name(j, f).split(".")[0]) in errorImgIDSet:
                error_coco_dict["annotations"].append(temp_dict)
    print("finished image bounding box data construction...")


bbox_df = img_boundingbox_data_constructor(
    os.path.join(train_folder, "digitStruct.mat")
)
with open(
    os.path.join(train_folder, "train_data_processed.json"), "w", encoding="utf-8"
) as f:
    json.dump(coco_dict, f, ensure_ascii=False)

with open(
    os.path.join(train_folder, "val_data_processed.json"), "w", encoding="utf-8"
) as f:
    json.dump(val_coco_dict, f, ensure_ascii=False)

with open(
    os.path.join(train_folder, "error_data_processed.json"), "w", encoding="utf-8"
) as f:
    json.dump(error_coco_dict, f, ensure_ascii=False)
