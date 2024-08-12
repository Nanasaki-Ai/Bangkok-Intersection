# Bangkok Intersection Dataset for Illegal Action Detection
This is the code for
**'How to Detect Non-yielding Actions of Vehicles?  A Challenging Dataset with Strong Baseline'.**

# Overview

&nbsp;&nbsp;&nbsp;&nbsp;· We introduce a public dataset for detecting vehicles that fail to yield to pedestrians. This dataset, the first of its kind, captures real traffic scenes at two zebra crossings at a Bangkok intersection and includes 10 hours of video containing 1972 instances of violations.

&nbsp;&nbsp;&nbsp;&nbsp;· We offer a new approach for understanding vehicle non-yielding behavior in surveillance videos. The filtering strategy transforms the task of detecting violations in complex scenes into recognizing violation actions within specific spatiotemporal regions of interest.

**The current versions are all available for download from Baidu Netdisk.**

## Bangkok Intersection Dataset

2024.08.12 The **[labels](https://pan.baidu.com/s/17_Zi4dSVOLou5N1yRG0Ilw?pwd=4o9a)** for training and testing are publicly available.

2024.08.11 The **[dataset](https://pan.baidu.com/s/1d2cyQVXj8Kc964-4tjYk4g?pwd=mn2s)**(52GB) and **[annotations](https://pan.baidu.com/s/1aoJLJUT-A7H4jO1Luzsp9w?pwd=6l8r)** are currently available for download.

&nbsp;&nbsp;&nbsp;&nbsp; See more details about the [dataset](#dataset-introduction) and annotations.

2024.07.23 The **[preprocessed features](#download-feature-table)** are currently available for download.

It is recommended to download the features of **stage #5** first for quick reproduction.

### Dataset Introduction

 This dataset originates from continuous 24-hour live-streams of a specific intersection in Bangkok, captured from a fixed overhead perspective on YouTube.
 
 It consists of 10 hours of footage, divided into 120 untrimmed videos, recorded between November 2023 and March 2024.
 
 Video numbers range from video_001 to video_120. All videos are five minutes long.
 
 These videos feature the same traffic scene under various weather conditions and times of day.
 
 Focusing on two pedestrian crosswalks, the dataset captures vehicles moving bidirectionally, entering and exiting the frame via the left and right boundaries.
 
 To reduce extraneous background activity, the recordings were confined to areas of interest, yielding a final video resolution of 1200×1100 pixels at 30 fps.

### Dataset Preparation

We divide the video into frames, which is also an important pre-step for subsequent preprocessing.

`pip install video-cli`

Take video_001 as an example and divide it into frames:

`video-toimg train_001.avi`

## Our Method

The overall process of this work is illustrated in <strong><a href="#figure1">Figure 1</a></strong>.

<strong><a href="#figure2">Figure 2</a></strong> visualizes the features (snippets) of different preprocessing stages.

<strong><a href="#table1">Table 1</a></strong> shows the different stages and their corresponding download links.

<hr style="width:50%;text-align:center;margin-left:auto;margin-right:auto;">

<p align="center">
  <img src="demo/overall_framework.jpg" alt="Figure 1. Our framework" id="figure1" width="1000"/>
</p>
<p align="center">
  <em><strong>Figure 1. Our framework.</strong></em>
</p>

<hr style="width:50%;text-align:center;margin-left:auto;margin-right:auto;">

 <p align="center" id="figure2">
  <img src="demo/stage_1_rgb.gif" alt="Stage #1" width="200"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="demo/stage_2_rgb.gif" alt="Stage #2" width="100"/>
</p>
 <p align="center">
  <img src="demo/stage_3_tra.gif" alt="Stage #3" width="200"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="demo/stage_4_tra.gif" alt="Stage #4" width="100"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="demo/stage_5_tra.gif" alt="Stage #5" width="100"/>
</p>
 <p align="center">
  <em><strong>Figure 2. Feature preprocessing visualization.</strong> For details on the specific stages of preprocessing, please refer to <strong><a href="#table1">Table 1</a></strong>.</em>
</p> 
 <p align="center">
  <em>The first row are video snippets. Left: Stage #1. Right: Stage #2.</em>
</p>  
 <p align="center">
  <em>The second row are trajectory snippets. Left: Stage #3. Middle: Stage #4. Right: Stage #5.</em>
</p>

<hr style="width:50%;text-align:center;margin-left:auto;margin-right:auto;">

  <p align="center" id="table1">
  <em><strong>Table 1. Preprocessing stage.</strong> For details on feature preprocessing visualization, please refer to <strong><a href="#figure2">Figure 2</a></strong>.</em>
</p> 
  <p align="center">
  <em>Method indicates the preprocessing scheme used. RBTF represents the region-based trajectories filtering operation, BR indicates background removal strategy, IVE means irrelevant vehicle elimination approach.</em>
</p> 

<div align="center">
  <table id="download-feature-table">
    <tr>
      <th>Stage</th>
      <th>Modality</th>
      <th>Method</th>
      <th>Download</th>
      <th>File(rar)</th>
      <th>Size</th>
    </tr>
    <tr>
      <td>#1</td>
      <td>Video</td>
      <td>None</td>
      <td><a href="https://pan.baidu.com/s/1fPxTRJlmCoPldaAI4bjjxA?pwd=btxe">Baidu Netdisk</a></td>
      <td>rgb_features</td>
      <td>31.4GB</td>
    </tr>
    <tr>
      <td>#2</td>
      <td>Video</td>
      <td>RBTF</td>
      <td><a href="https://pan.baidu.com/s/1JVXRf5kXREh3a1REQBJwUQ?pwd=m4r4">Baidu Netdisk</a></td>
      <td>rgb_volumes_region</td>
      <td>11.9GB</td>
    </tr>
    <tr>
      <td>#3</td>
      <td>Trajectory</td>
      <td>BR</td>
      <td><a href="https://pan.baidu.com/s/19fNUNXKMrWR-E5vOMNY2Og?pwd=kueg">Baidu Netdisk</a></td>
      <td>tra_features</td>
      <td>974MB</td>
    </tr>
    <tr>
      <td>#4</td>
      <td>Trajectory</td>
      <td>RBTF+BR</td>
      <td><a href="https://pan.baidu.com/s/1_pXS_LDc4hPn03LPwgrEkw?pwd=06lp">Baidu Netdisk</a></td>
      <td>tra_volumes_region</td>
      <td>522MB</td>
    </tr>
    <tr>
      <td>#5</td>
      <td>Trajectory</td>
      <td>RBTF+BR+IVE</td>
      <td><a href="https://pan.baidu.com/s/13Dpw9sfgvsDdlwnGUtXGgw?pwd=1esm">Baidu Netdisk</a></td>
      <td>tra_att_volumes_region</td>
      <td>410MB</td>
    </tr>
  </table>
</div>

<hr style="width:50%;text-align:center;margin-left:auto;margin-right:auto;">

# Pretrained Detector

To accurately detect objects of interest in traffic scenes, we use YOLOv8-m for pre-training on additional annotated datasets.

We recommend using the provided datasets for object detector training or utilizing the trained model parameters.

This additional [auxiliary dataset](https://app.roboflow.com/nnu-hi7if/nnu_intersection/7) is used to train the object detector.

Please install the environment according to the official website of [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics/blob/main/README.md).

All models were trained on an RTX 4090. You can use our [pretrained weights](https://pan.baidu.com/s/1XhjA8IiR8zNuU3blHsymEQ?pwd=z8fl) or train the model yourself.

Training a detector from scratch：

`yolo task=detect mode=train model=yolov8m.pt data=intersection_images/data.yaml epochs=100 imgsz=640`

YOLOv8 has five variants: -n, -s, -m, -l, -x. The "model" parameter can be modified to specify the variant to use.

We recommend using -m as it achieves better results on auxiliary datasets.

# Prepeocessing Method


# Acknowledgments

We would like to express our sincere gratitude to the following individuals and groups for their invaluable assistance in this work:

&nbsp;&nbsp;&nbsp;&nbsp;· The person in charge of the YouTube live broadcast platform for permitting data collection.

&nbsp;&nbsp;&nbsp;&nbsp;· The officers in Nanjing Transport for their meticulous annotation of the dataset.

&nbsp;&nbsp;&nbsp;&nbsp;· Potential contributors, including reviewers and researchers, for their interest and input in this work.

# Contact

Any questions, feel free to contact me via email: `zeshenghu@njnu.edu.cn`
