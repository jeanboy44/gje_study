import os
from glob import glob
import warnings

import numpy as np
import pandas as pd
from tqdm import tqdm

import matplotlib as mpl
from matplotlib import pyplot as plt 

import cv2

warnings.filterwarnings("ignore", category=UserWarning)

pd.set_option('display.float_format', '{:.2f}'.format)
pd.set_option('display.max_columns', 500)

%matplotlib inline

img_sample = cv2.imread("data/dataset100/UECFOOD100/1/4.jpg")

plt.figure(figsize = (14, 14))
plt.imshow(cv2.cvtColor(img_sample, cv2.COLOR_BGR2RGB))

label_sample = pd.read_csv("data/dataset100/UECFOOD100/1/bb_info.txt", sep = " ")

label_sample[label_sample["img"] == 4]

cv2.rectangle(img_sample, label_sample[label_sample["img"] == 4], 2)
