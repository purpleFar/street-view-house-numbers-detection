# Street View House Numbers Detection
<p align="left">
    <a>
        <img src=https://img.shields.io/badge/python-3.6.12-green>
    </a>
    <a>
        <img src=https://img.shields.io/badge/pytorch-1.7.0-orange>
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>

This repository gathers is the code for homework in class.
To read the detailed for what is this, please, refer to [my report](https://github.com/purpleFar/street-view-house-numbers-detection/blob/master/readme_file/HW2%20Report_0856735.pdf).

## Hardware
The following specs were used to create the original solution.
- Windows 10
- Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz 2.50GHz
- NVIDIA GeForce GTX 1660 Ti

## Outline
To reproduct my result without retrainig, do the following steps:
1. [Installation](#installation)
2. [Download Data](#download-data)
3. [Preprocessing Images](#preprocessing-images)
4. [Download Pretrained models](#pretrained-models)
5. [Inference](#inference)

## Installation
See [this](https://github.com/purpleFar/street-view-house-numbers-detection/blob/master/orgREADME.md) to know how to use mmdetection.
And [here](https://github.com/purpleFar/street-view-house-numbers-detection/blob/master/get_started.md) is how to install it.

## Download Data
The street view house numbers data download at [here](https://github.com/pavitrakumar78/Street-View-House-Numbers-SVHN-Detection-and-Classification-using-CNN/blob/master/construct_datasets.py).
Unzip them then you can see following structure:
```
street-view-house-numbers-detection/
    ├── train
    │   ├── 1.png
    │   ├── 2.png
    │   │   .
    │   │   .
    │   │   .
    │   ├── 33402.png
    │   ├── digitStruct.mat
    │   └── see_bboxes.m
    ├── test
    │   ├── 1.png
    │   ├── 2.png
    │   │   .
    │   │   .
    │   │   .
    │   └── 13068.png
    ├── to_coco_format.py
    │   .
    │   .
```

## Preprocessing Images
To train or inference, transfer the data fomat to coco format is required. Run following command.
```bash=
$ python to_coco_format.py
```
then there is some file in preprocess_file folder like this
```
street-view-house-numbers-detection/train/
    ├── 1.png
    ├── 2.png
    │   .
    │   .
    │   .
    ├── 33402.png
    ├── digitStruct.mat
    ├── see_bboxes.m
    ├── train_data_processed.json
    ├── val_data_processed.json
    └── error_data_processed.json
```

## Train models
To train models, run following command.
```bash=
$ python tool/train.py config/faster_rcnn/faster_rcnn_r34_fpn_1x_coco.py
```

## Pretrained models
You can download pretrained model that used for my submission from [link](https://drive.google.com/file/d/1XkKurOTGL-PFJfLlPGpkKmwGintVcT04/view?usp=sharing). Or run following commands.

**Note!** there is no default unzip command in windows 10, you must unzip by GUI.
```bash=
$ wget https://drive.google.com/file/d/1XkKurOTGL-PFJfLlPGpkKmwGintVcT04/view?usp=sharing
$ unzip model_wide_resnet.zip
```
Unzip them and put then in structure:
```
street-view-house-numbers-detection/work_dirs/
    └── faster_rcnn_r34_fpn_1x_coco
        └── latest.pth
```

## Inference
If trained weights are prepared, you can create a file containing the bboxes for each picture in test set.

Using the pre-trained model, enter the command:
```bash=
$ python inference_demo.py
```
And you can see the 0856735_xx.json in result folder