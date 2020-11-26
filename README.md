# car-brand-classification
<p align="left">
    <a>
        <img src=https://img.shields.io/badge/python-3.6.12-green>
    </a>
    <a>
        <img src=https://img.shields.io/badge/pytorch-1.5.0-orange>
    </a>
    <a>
        <img src=https://img.shields.io/badge/Imgaug-0.4.0-red>
    </a>
    <a href="https://github.com/psf/black">
        <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
    </a>
</p>

This repository gathers the code for car brand classification from the [in-class Kaggle challenge](https://www.kaggle.com/c/cs-t0828-2020-hw1).  
To read the detailed solution, please, refer to [my report](https://github.com/purpleFar/car-brand-classification/blob/master/readme_file/HW1%20Report_0856735.pdf).

## Hardware
The following specs were used to create the original solution.
- Windows 10
- Intel(R) Core(TM) i5-10300H CPU @ 2.50GHz 2.50GHz
- NVIDIA GeForce GTX 1660 Ti

## Reproducing Submission
To reproduct my submission without retrainig, do the following steps:
1. [Installation](#installation)
2. [Download Data](#download-data)
3. [Preprocessing Images](#preprocessing-images)
4. [Download Pretrained models](#pretrained-models)
5. [Inference](#inference)

## Installation
All requirements should be detailed in requirements.txt. Using Anaconda is strongly recommended.
```bash=
$ conda create -n  hw1 python=3.6
$ conda activate hw1
$ pip install -r requirements.txt
```

## Download Data
If the Kaggle API is installed, run following commands.

**Note!** there is no default unzip command in windows 10, you must unzip by GUI.
```bash=
$ kaggle competitions download -c cs-t0828-2020-hw1
$ unzip cs-t0828-2020-hw1.zip
```
Unzip them then you can see following structure:
```
car-brand-classification/
    ├── testing_data
    │   ├── 000004.jpg
    │   ├── 000005.jpg
    │   │   .
    │   │   .
    │   │   .
    │   └── 016181.jpg
    ├── training_data
    │   ├── 000001.jpg
    │   ├── 000002.jpg
    │   │   .
    │   │   .
    │   │   .
    │   └── 016185.jpg
    ├── training_labels.csv
    │   .
    │   .
```

## Preprocessing Images
To train or inference, preprocessing is required. Run following command.
```bash=
$ python preprocessing.py
```
then there is some file in preprocess_file folder
like this
```
car-brand-classification/preprocess_file/
    ├── label.pkl
    ├── name_to_num.pkl
    └── num_to_name.pkl
```

## Train models
To train models, run following command.
```bash=
$ python train.py --train_dir training_data --model_save_dir model
```

## Pretrained models
You can download pretrained model that used for my submission from [link](https://drive.google.com/file/d/1fkrZNX9LAD8Ro5DOyG-Qap0MxV9LOLmH/view?usp=sharing). Or run following commands.

**Note!** there is no default unzip command in windows 10, you must unzip by GUI.
```bash=
$ wget https://drive.google.com/file/d/1fkrZNX9LAD8Ro5DOyG-Qap0MxV9LOLmH/view?usp=sharing
$ unzip model_wide_resnet.zip
```
Unzip them then you can see following structure:
```
car-brand-classification/model_wide_resnet/
    ├── best_model0.pt
    ├── best_model1.pt
    ├── best_model2.pt
    ├── best_model3.pt
    ├── best_model4.pt
    ├── best_model5.pt
    ├── best_model6.pt
    ├── best_model7.pt
    ├── best_model8.pt
    ├── best_model9.pt
    ├── best_model10.pt
    ├── best_model11.pt
    └── best_model12.pt
```

## Inference
If trained weights are prepared, you can create a file containing the car brand classification for each picture in test set.

Using the model trained by yourself, enter the command:
```bash=
$ python test.py --test_dir testing_data --model_dir model --save_name submission.csv
```
Using the pre-trained model, enter the command:
```bash=
$ python test.py --test_dir testing_data --model_dir model_wide_resnet --save_name submission.csv
```
And you can see the submission.csv in result folder