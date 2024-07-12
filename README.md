# Bangkok Intersection Dataset for Illegal Action Detection
This is the code for
**'How to Detect Non-yielding Actions of Vehicles?  A Challenging Dataset with Strong Baseline'.**

# Overview

&nbsp;&nbsp;&nbsp;&nbsp;· We introduce a public dataset for detecting vehicles that fail to yield to pedestrians. This dataset, the first of its kind, captures real traffic scenes at two zebra crossings at a Bangkok intersection and includes 10 hours of video containing 1972 instances of violations.

&nbsp;&nbsp;&nbsp;&nbsp;· We offer a new approach for understanding vehicle non-yielding behavior in surveillance videos. The filtering strategy transforms the task of detecting violations in complex scenes into recognizing violation actions within specific spatiotemporal regions of interest.

## Bangkok Intersection Dataset

The dataset will be released in a subsequent update, while the preprocessed mid-level features are currently available for download.

## Our Method

The overall process of this work is illustrated in Figure 1.

<p align="center">
  <img src="demo/overall_framework.jpg" alt="Figure 1. Our framework" width="1000"/>
</p>
 <p align="center">
  <em>Figure 1. Our framework.</em>
</p>

 <p align="center">
  <img src="demo/stage_1_rgb.gif" alt="Original video snippets" width="300"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="demo/stage_2_rgb.gif" alt="Stage #2" width="200"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="demo/stage_4_tra.gif" alt="Stage #4" width="200"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="demo/stage_5_tra.gif" alt="Stage #5" width="200"/>
</p>
 <p align="center">
  <em>Figure 2. Feature preprocessing visualization.</em>
</p>
# Pretrained Detector

To accurately detect objects of interest in traffic scenes, we use YOLOv8-m for pre-training on additional annotated datasets.

We recommend using the provided datasets for object detector training or utilizing the trained model parameters.

# Prepeocessing Method


# Acknowledgments

We would like to express our sincere gratitude to the following individuals and groups for their invaluable assistance in this work:

&nbsp;&nbsp;&nbsp;&nbsp;· The person in charge of the YouTube live broadcast platform for permitting data collection.

&nbsp;&nbsp;&nbsp;&nbsp;· The officers in Nanjing Transport for their meticulous annotation of the dataset.

&nbsp;&nbsp;&nbsp;&nbsp;· Potential contributors, including reviewers and researchers, for their interest and input in this work.

# Contact

Any questions, feel free to contact me via email: `zeshenghu@njnu.edu.cn`
